import logging

from django.dispatch import receiver

from django_ynh.sso_auth.signals import setup_user


logger = logging.getLogger(__name__)


@receiver(setup_user)
def setup_user_handler(sender, **kwargs):
    """
    Make user to a "staff" user, so he can use the Django admin.

    This Signal is called via:
     * SSOwatUserBackend after a new user was created
     * SSOwatRemoteUserMiddleware on login request
    """
    user = kwargs['user']
    logger.info('Receive "setup_user" signal for user: "%s"', user)

    if not user.is_staff:
        user.is_staff = True
        user.save(update_fields=['is_staff'])
        logger.info('Make user %s to a staff user', user)
