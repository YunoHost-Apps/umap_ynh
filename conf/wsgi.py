"""
    WSGI config
"""
import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'django_ynh.settings'

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
