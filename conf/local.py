from pathlib import Path as __Path
import os

# ==============================================================================
# 1. LOAD UMAP DEFAULTS
# ==============================================================================
from umap.settings.base import *

_umap_apps = list(INSTALLED_APPS)
_umap_middleware = list(MIDDLEWARE)
_umap_backends = list(AUTHENTICATION_BACKENDS)

# ==============================================================================
# 2. LOAD YUNOHOST INTEGRATION
# ==============================================================================
from django_yunohost_integration.base_settings import *

# ==============================================================================
# 3. Restore missing uMap settings
# ==============================================================================

for app in _umap_apps:
    if app not in INSTALLED_APPS:
        INSTALLED_APPS.append(app)

for mw in _umap_middleware:
    if mw not in MIDDLEWARE:
        MIDDLEWARE.append(mw)

for backend in _umap_backends:
    if backend not in AUTHENTICATION_BACKENDS:
        AUTHENTICATION_BACKENDS += (backend,)

#if 'django_yunohost_integration' not in INSTALLED_APPS:
#    INSTALLED_APPS.append('django_yunohost_integration')

ROOT_URLCONF = 'umap.urls' 
LOG_LEVEL = "INFO"

# ==============================================================================
# YunoHost Path & Setup
# ==============================================================================

# Data Directory: /home/yunohost.app/$app
DATA_DIR_PATH = __Path('__DATA_DIR__')
if str(DATA_DIR_PATH) != '__DATA_DIR__' and not DATA_DIR_PATH.is_dir():
    print(f"Warning: Directory does not exist: {DATA_DIR_PATH}")

# Install Directory: /var/www/$app
INSTALL_DIR_PATH = __Path('__INSTALL_DIR__')

# Log File: /var/log/$app/$app.log
LOG_FILE = __Path('/var/log/__APP__/__APP__.log')

# URL Path
PATH_URL = '__PATH_URL__'
PATH_URL = PATH_URL.strip('/')

# ==============================================================================
# Core Security & Configuration
# ==============================================================================

# SECRET_KEY, override :-
if str(DATA_DIR_PATH) != '__DATA_DIR__':
    SECRET_KEY = __get_or_create_secret(DATA_DIR_PATH / 'secret.txt')

# DEBUG
DEBUG = False

# Hosts & Domains
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "__DOMAIN__"]

INTERNAL_IPS = ["127.0.0.1"]

# CSRF
CSRF_TRUSTED_ORIGINS = ["https://__DOMAIN____PATH__"]

# Language
LANGUAGE_CODE = "__LANGUAGE_CODE__"

# Admins
ADMINS = (("__ADMIN__", __ADMIN_MAIL__),)

MANAGERS = ADMINS

# ==============================================================================
# Database (PostGIS)
# ==============================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "__DB_NAME__",
        "USER": "__DB_USER__",
        "PASSWORD": "__DB_PWD__",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# ==============================================================================
# YunoHost Integration App & Middleware
# ==============================================================================

# Insert SSO Middleware after standard AuthenticationMiddleware
try:
    auth_mw_index = MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware')
    MIDDLEWARE.insert(
        auth_mw_index + 1,
        'django_yunohost_integration.sso_auth.auth_middleware.SSOwatRemoteUserMiddleware',
    )
except ValueError:
    MIDDLEWARE.append('django_yunohost_integration.sso_auth.auth_middleware.SSOwatRemoteUserMiddleware')

# Authentication Backends
AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesBackend',
    'django_yunohost_integration.sso_auth.auth_backend.SSOwatUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Login/Logout Behavior
LOGIN_REDIRECT_URL = None
LOGIN_URL = '/yunohost/sso/'
LOGOUT_REDIRECT_URL = '/yunohost/sso/'

# Helper for user creation
YNH_SETUP_USER = 'setup_user.setup_project_user'

# ==============================================================================
# Static & Media Files
# ==============================================================================

STATIC_ROOT = "static"

MEDIA_ROOT = DATA_DIR_PATH / 'data'
UMAP_CUSTOM_STATICS = DATA_DIR_PATH / 'custom/static'
UMAP_CUSTOM_TEMPLATES = DATA_DIR_PATH / 'custom/templates'

# ==============================================================================
# uMap Specific Settings
# ==============================================================================

SITE_URL = "http://__DOMAIN____PATH__"
SHORT_SITE_URL = "none"
SITE_NAME = "__SITE_NAME__"

UMAP_ALLOW_ANONYMOUS = __UMAP_ALLOW_ANONYMOUS__
UMAP_ALLOW_EDIT_PROFILE = __UMAP_ALLOW_EDIT_PROFILE__
UMAP_KEEP_VERSIONS = "__UMAP_KEEP_VERSIONS__"
UMAP_READONLY = __UMAP_READONLY__
ENABLE_ACCOUNT_LOGIN = __ENABLE_ACCOUNT_LOGIN__
REALTIME_ENABLED = __REALTIME_ENABLED__

UMAP_DEMO_SITE = False
USER_AUTOCOMPLETE_FIELDS = ["^username", "email"]
USER_DISPLAY_NAME = "{username}"

UMAP_DEFAULT_EDIT_STATUS = "__UMAP_DEFAULT_EDIT_STATUS__"
UMAP_DEFAULT_SHARE_STATUS = "__UMAP_DEFAULT_SHARE_STATUS__"
UMAP_HOME_FEED = "__UMAP_HOME_FEED__"

# ==============================================================================
# Services (Redis, Email, Social Auth)
# ==============================================================================

# Redis
REDIS_URL = "redis://localhost:6379/__REDIS_DB__"

# Email
EMAIL_HOST = "__DOMAIN__"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "__MAIL_USER__"
EMAIL_HOST_PASSWORD = "__MAIL_PWD__"
DEFAULT_FROM_EMAIL = "__MAIL_USER__@__DOMAIN__"
SERVER_EMAIL = "__MAIL_USER__@__DOMAIN__"

# Social Auth
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# Other settings, to add
# SOCIAL_AUTH_OPENSTREETMAP_OAUTH2_KEY = ...
# SOCIAL_AUTH_OPENSTREETMAP_OAUTH2_SECRET = ...
