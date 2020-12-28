"""
    "setup_user" called via:

        * SSOwatUserBackend after a new user was created
        * SSOwatRemoteUserMiddleware on login request
"""


import django.dispatch


setup_user = django.dispatch.Signal(providing_args=['user'])
