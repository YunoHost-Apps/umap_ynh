"""
    WSGI config
"""
import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'django_ynh_demo_settings'

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
