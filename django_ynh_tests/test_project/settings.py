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



ROOT_URLCONF = 'django_ynh_tests.test_project.urls'



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


