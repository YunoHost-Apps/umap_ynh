from pathlib import Path as __Path
from .base import *
from django_yunohost_integration.base_settings import *

DATA_DIR_PATH = __Path('__DATA_DIR__') 
if str(DATA_DIR_PATH) != '__DATA_DIR__' and not DATA_DIR_PATH.is_dir():
     print(f"Warning: Directory not exists: {DATA_DIR_PATH}")

INSTALL_DIR_PATH = __Path('__INSTALL_DIR__')

LOG_FILE = __Path('/var/log/__APP__/__APP__.log')

PATH_URL = '__PATH_URL__'
PATH_URL = PATH_URL.strip('/')

from django_yunohost_integration.secret_key import get_or_create_secret as __get_or_create_secret
if str(DATA_DIR_PATH) != '__DATA_DIR__':
    SECRET_KEY = __get_or_create_secret(DATA_DIR_PATH / 'secret.txt')

INSTALLED_APPS.append('django_yunohost_integration')

try:
    auth_mw_index = MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware')
    MIDDLEWARE.insert(
        auth_mw_index + 1,
        'django_yunohost_integration.sso_auth.auth_middleware.SSOwatRemoteUserMiddleware',
    )
except ValueError:
    MIDDLEWARE.append('django_yunohost_integration.sso_auth.auth_middleware.SSOwatRemoteUserMiddleware')

AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesBackend',
    'django_yunohost_integration.sso_auth.auth_backend.SSOwatUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = None
LOGIN_URL = '/yunohost/sso/'
LOGOUT_REDIRECT_URL = '/yunohost/sso/'

YNH_SETUP_USER = 'setup_user.setup_project_user'

# ROOT_URLCONF = 'urls'
