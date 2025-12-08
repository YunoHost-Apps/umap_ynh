#!/usr/bin/env python3
"""
Here it's possible to overwrite everything in settings.py

Note:
    Used for YunoHost config and will be **overwritten** on every config change!
"""

from umap.settings.base import *  # noqa

from pathlib import Path

DEBUG = __DJANGO_DEBUG__  # noqa Don't turn DEBUG on in production!
STATIC_ROOT = Path("__DATA_DIR__") / "static"  # noqa
MEDIA_ROOT = Path("__DATA_DIR__") / "data"  # noqa

INSTALLED_APPS.append("django_yunohost_integration")  # noqa

MIDDLEWARE.insert(
    MIDDLEWARE.index("django.contrib.auth.middleware.AuthenticationMiddleware") + 1,
    # login a user via HTTP_REMOTE_USER header from SSOwat:
    "django_yunohost_integration.sso_auth.auth_middleware.SSOwatRemoteUserMiddleware",
)

# Keep ModelBackend around for per-user permissions and superuser
AUTHENTICATION_BACKENDS = (
    "axes.backends.AxesBackend",  # AxesBackend should be the first backend!
    #
    # Authenticate via SSO and nginx 'HTTP_REMOTE_USER' header:
    "django_yunohost_integration.sso_auth.auth_backend.SSOwatUserBackend",
    #
    # Fallback to normal Django model backend:
    "django.contrib.auth.backends.ModelBackend",
)

LOGIN_REDIRECT_URL = None
LOGIN_URL = "/yunohost/sso/"
LOGOUT_REDIRECT_URL = "/yunohost/sso/"
