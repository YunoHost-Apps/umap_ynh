"""
    urls.py
    ~~~~~~~

    Note: This is not a good example how your urls.py can look like.
          Because this setup is just an example without a real Python application.

    Look at real examples, here:

     * https://github.com/YunoHost-Apps/django-fritzconnection_ynh/blob/master/conf/urls.py
     * https://github.com/YunoHost-Apps/django-for-runners_ynh/blob/testing/conf/urls.py
     * https://github.com/YunoHost-Apps/pyinventory_ynh/blob/testing/conf/urls.py

"""


from django.conf import settings
from django.contrib import admin
from django.urls import path

from django_yunohost_integration.views import request_media_debug_view


if settings.PATH_URL:
    # settings.PATH_URL is the $YNH_APP_ARG_PATH
    # Prefix all urls with "PATH_URL":
    urlpatterns = [
        path(f'{settings.PATH_URL}/debug/', request_media_debug_view),
        path(f'{settings.PATH_URL}/', admin.site.urls),
    ]
else:
    # Installed to domain root, without a path prefix
    urlpatterns = [
        path('debug/', request_media_debug_view),
        path('', admin.site.urls),
    ]
