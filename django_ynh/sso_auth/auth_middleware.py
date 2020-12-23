import base64
import logging

from axes.exceptions import AxesBackendPermissionDenied
from django.contrib.auth.middleware import RemoteUserMiddleware


logger = logging.getLogger(__name__)


class SSOwatRemoteUserMiddleware(RemoteUserMiddleware):
    """
    Middleware to login a user HTTP_REMOTE_USER header.
    Use Django Axes if something is wrong.
    Update exising user informations.
    """

    header = 'HTTP_REMOTE_USER'
    force_logout_if_no_header = True

    def process_request(self, request):
        # Keep the information if the user is already logged in
        was_authenticated = request.user.is_authenticated

        super().process_request(request)  # login remote user

        if not request.user.is_authenticated:
            # Not logged in -> nothing to verify here
            return

        # Check SSOwat cookie informations:
        try:
            username = request.COOKIES['SSOwAuthUser']
        except KeyError:
            logger.error('SSOwAuthUser cookie missing!')

            # emits a signal indicating user login failed, which is processed by
            # axes.signals.log_user_login_failed which logs and flags the failed request.
            raise AxesBackendPermissionDenied('Cookie missing')

        logger.info('SSOwat username from cookies: %r', username)
        if username != request.user.username:
            raise AxesBackendPermissionDenied('Wrong username')

        # Compare with HTTP_AUTH_USER
        try:
            username = request.META['HTTP_AUTH_USER']
        except KeyError:
            logger.error('HTTP_AUTH_USER missing!')
            raise AxesBackendPermissionDenied('No HTTP_AUTH_USER')

        if username != request.user.username:
            raise AxesBackendPermissionDenied('Wrong HTTP_AUTH_USER username')

        # Also check 'HTTP_AUTHORIZATION', but only the username ;)
        try:
            auth = request.META['HTTP_AUTHORIZATION']
        except KeyError:
            logger.error('HTTP_AUTHORIZATION missing!')
            raise AxesBackendPermissionDenied('No HTTP_AUTHORIZATION')

        scheme, creds = auth.split(' ', 1)
        if scheme.lower() != 'basic':
            logger.error('HTTP_AUTHORIZATION with %r not supported', scheme)
            raise AxesBackendPermissionDenied('HTTP_AUTHORIZATION scheme not supported')

        creds = str(base64.b64decode(creds), encoding='utf-8')
        username = creds.split(':', 1)[0]
        if username != request.user.username:
            raise AxesBackendPermissionDenied('Wrong HTTP_AUTHORIZATION username')

        if not was_authenticated:
            # First request, after login -> update user informations
            logger.info('Remote used was logged in')
            update_user_profile(request)
