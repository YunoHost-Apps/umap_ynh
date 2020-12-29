# django_ynh

Current state is broken, because we are **planing** ;)

[![Integration level](https://dash.yunohost.org/integration/django_ynh.svg)](https://dash.yunohost.org/appci/app/django_ynh) ![](https://ci-apps.yunohost.org/ci/badges/django_ynh.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/django_ynh.maintain.svg)
[![Install django_ynh with YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django_ynh)

> *This package allows you to install django_ynh quickly and simply on a YunoHost server.
If you don't have YunoHost, please consult [the guide](https://yunohost.org/#/install) to learn how to install it.*

Pull requests welcome ;)


## Overview

Glue code to package django projects as yunohost apps.

This project is:

* The Python package [django-ynh](https://pypi.org/project/django-ynh/) with helpers for integrate a Django project as YunoHost package
* A example YunoHost Application that can be installed
* Run Django development server with a local generated YunoHost package installation (called `local_test`)


### usage

To create/update a the first user in `install`/`upgrade`, e.g.:

```bash
./manage.py create_superuser --username="$admin" --email="$admin_mail"
```
This Create/update Django superuser and set a unusable password.
A password is not needed, because auth done via SSOwat ;)


## SSO authentication

[SSOwat](https://github.com/YunoHost/SSOwat) is fully supported:

* First user (`$YNH_APP_ARG_ADMIN`) will be created as Django's super user
* All new users will be created as normal users
* Login via SSO is fully supported
* User Email, First / Last name will be updated from SSO data


## history

* [compare v0.1.0...master](https://github.com/YunoHost-Apps/django_ynh/compare/v0.1.0...master) **dev**
  * tbc
* [v0.1.0 - 28.12.2020](https://github.com/YunoHost-Apps/django_ynh/compare/f578f14...v0.1.0)
  * first working state
* [23.12.2020](https://github.com/YunoHost-Apps/django_ynh/commit/f578f144a3a6d11d7044597c37d550d29c247773)
  * init the project


## Links

 * Report a bug about this package: https://github.com/YunoHost-Apps/django_ynh
 * YunoHost website: https://yunohost.org/

---

# Developer info

## package installation / debugging

Please send your pull request to https://github.com/YunoHost-Apps/django_ynh

Try 'main' branch, e.g.:
```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django_ynh/tree/master --debug
or
sudo yunohost app upgrade django_ynh -u https://github.com/YunoHost-Apps/django_ynh/tree/master --debug
```

Try 'testing' branch, e.g.:
```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django_ynh/tree/testing --debug
or
sudo yunohost app upgrade django_ynh -u https://github.com/YunoHost-Apps/django_ynh/tree/testing --debug
```

To remove call e.g.:
```bash
sudo yunohost app remove django_ynh
```

Backup / remove / restore cycle, e.g.:
```bash
yunohost backup create --apps django_ynh
yunohost backup list
archives:
  - django_ynh-pre-upgrade1
  - 20201223-163434
yunohost app remove django_ynh
yunohost backup restore 20201223-163434 --apps django_ynh
```

Debug installation, e.g.:
```bash
root@yunohost:~# ls -la /var/www/django_ynh/
total 18
drwxr-xr-x 4 root root 4 Dec  8 08:36 .
drwxr-xr-x 6 root root 6 Dec  8 08:36 ..
drwxr-xr-x 2 root root 2 Dec  8 08:36 media
drwxr-xr-x 7 root root 8 Dec  8 08:40 static

root@yunohost:~# ls -la /opt/yunohost/django_ynh/
total 58
drwxr-xr-x 5 django_ynh django_ynh   11 Dec  8 08:39 .
drwxr-xr-x 3 root        root           3 Dec  8 08:36 ..
-rw-r--r-- 1 django_ynh django_ynh  460 Dec  8 08:39 gunicorn.conf.py
-rw-r--r-- 1 django_ynh django_ynh    0 Dec  8 08:39 local_settings.py
-rwxr-xr-x 1 django_ynh django_ynh  274 Dec  8 08:39 manage.py
-rw-r--r-- 1 django_ynh django_ynh  171 Dec  8 08:39 secret.txt
drwxr-xr-x 6 django_ynh django_ynh    6 Dec  8 08:37 venv
-rw-r--r-- 1 django_ynh django_ynh  115 Dec  8 08:39 wsgi.py
-rw-r--r-- 1 django_ynh django_ynh 4737 Dec  8 08:39 django_ynh_demo_settings.py

root@yunohost:~# cd /opt/yunohost/django_ynh/
root@yunohost:/opt/yunohost/django_ynh# source venv/bin/activate
(venv) root@yunohost:/opt/yunohost/django_ynh# ./manage.py check
django_ynh v0.8.2 (Django v2.2.17)
DJANGO_SETTINGS_MODULE='django_ynh_demo_settings'
PROJECT_PATH:/opt/yunohost/django_ynh/venv/lib/python3.7/site-packages
BASE_PATH:/opt/yunohost/django_ynh
System check identified no issues (0 silenced).

root@yunohost:~# tail -f /var/log/django_ynh/django_ynh.log
root@yunohost:~# cat /etc/systemd/system/django_ynh.service

root@yunohost:~# systemctl reload-or-restart django_ynh
root@yunohost:~# journalctl --unit=django_ynh --follow
```

## local test

For quicker developing of django_ynh in the context of YunoHost app,
it's possible to run the Django developer server with the settings
and urls made for YunoHost installation.

e.g.:
```bash
~$ git clone https://github.com/YunoHost-Apps/django_ynh.git
~$ cd django_ynh/
~/django_ynh$ make
install-poetry         install or update poetry
install                install django_ynh via poetry
update                 update the sources and installation
local-test             Run local_test.py to run django_ynh locally
~/django_ynh$ make install-poetry
~/django_ynh$ make install
~/django_ynh$ make local-test
```

Notes:

* SQlite database will be used
* A super user with username `test` and password `test` is created
* The page is available under `http://127.0.0.1:8000/app_path/`
