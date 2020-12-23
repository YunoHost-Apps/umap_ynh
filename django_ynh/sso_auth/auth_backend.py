"""
    remote user authentication backend

    Note: SSOwat/nginx add authentication headers:

        'HTTP_AUTHORIZATION': 'Basic XXXXXXXXXXXXXXXX='
        'HTTP_AUTH_USER': 'username'
        'HTTP_REMOTE_USER': 'username'

    Basic auth contains "{username}:{plaintext-password}"

    and we get SSOwat cookies like:

         'HTTP_COOKIE': 'SSOwAuthUser=username; '
                        'SSOwAuthHash=593876aa66...99e69f88af1e; '
                        'SSOwAuthExpire=1609227697.998; '

    * Login a user via HTTP_REMOTE_USER header, but check also username in:
        * SSOwAuthUser
        * HTTP_AUTH_USER
        * HTTP_AUTHORIZATION (Basic auth)
    * Create new users
    * Update Email, First / Last name for existing users
"""

import logging

from django.contrib.auth.backends import RemoteUserBackend

from django_ynh.sso_auth.user_profile import update_user_profile


logger = logging.getLogger(__name__)


class SSOwatUserBackend(RemoteUserBackend):
    """
    Authentication backend via SSO/nginx header
    """

    create_unknown_user = True

    def authenticate(self, request, remote_user):
        logger.info('Remote user authenticate: %r', remote_user)
        return super().authenticate(request, remote_user)

    def configure_user(self, request, user):
        """
        Configure a user after creation and return the updated user.
        Setup a normal, non-superuser
        """
        logger.warning('Configure user %s', user)

        user.set_unusable_password()  # Always login via SSO
        user.is_staff = True
        user.is_superuser = False
        user.save()

        # TODO: Add user in "normal" user group:
        # django_ynh_user_group = get_or_create_normal_user_group()[0]
        # user.groups.set([django_ynh_user_group])

        update_user_profile(request)

        return user

    def user_can_authenticate(self, user):
        logger.warning('Remote user login: %s', user)
        return True
