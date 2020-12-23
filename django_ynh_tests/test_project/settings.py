from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


SECRET_KEY = 'Only a test project!'


DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ynh',  # <<<<
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_ynh.sso_auth.auth_middleware.SSOwatRemoteUserMiddleware',  # <<<<
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_ynh_tests.test_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_ynh_tests.test_project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = []  # Just a test project, so no restrictions


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (BASE_DIR.parent / 'django_ynh' / 'locale',)


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


INTERNAL_IPS = [
    '127.0.0.1',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {name} {module}.{funcName} {message}',
            'style': '{',
        },
    },
    'handlers': {'console': {'class': 'logging.StreamHandler', 'formatter': 'verbose'}},
    'loggers': {
        'django': {'handlers': ['console'], 'level': 'INFO', 'propagate': False},
        'django.auth': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': False},
        'django.security': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': False},
        'django.request': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': False},
        'django_ynh': {'handlers': ['console'], 'level': 'DEBUG', 'propagate': False},
    },
}
