import base64
import logging

from axes.exceptions import AxesBackendPermissionDenied
from django.contrib.auth.backends import RemoteUserBackend as OriginRemoteUserBackend
from django.contrib.auth.middleware import RemoteUserMiddleware as OriginRemoteUserMiddleware
from django.core.exceptions import ValidationError
from inventory.permissions import get_or_create_normal_user_group


logger = logging.getLogger(__name__)


def update_user_profile(request):
    """
    Update existing user information:
     * Email
     * First / Last name
    """
    user = request.user
    assert user.is_authenticated

    update_fields = []

    if not user.password:
        # Empty password is not valid, so we can't save the model, because of full_clean() call
        logger.info('Set unusable password for user: %s', user)
        user.set_unusable_password()
        update_fields.append('password')

    email = request.META.get('HTTP_EMAIL')
    if email and user.email != email:
        logger.info('Update email: %r -> %r', user.email, email)
        user.email = email
        update_fields.append('email')

    raw_username = request.META.get('HTTP_NAME')
    if raw_username:
        if ' ' in raw_username:
            first_name, last_name = raw_username.split(' ', 1)
        else:
            first_name = ''
            last_name = raw_username

        if user.first_name != first_name:
            logger.info('Update first name: %r -> %r', user.first_name, first_name)
            user.first_name = first_name
            update_fields.append('first_name')

        if user.last_name != last_name:
            logger.info('Update last name: %r -> %r', user.last_name, last_name)
            user.last_name = last_name
            update_fields.append('last_name')

    if update_fields:
        try:
            user.full_clean()
        except ValidationError:
            logger.exception('Can not update user: %s', user)
        else:
            user.save(update_fields=update_fields)
