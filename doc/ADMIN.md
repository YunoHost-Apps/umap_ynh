## Settings and upgrades

Almost everything related to Django Example's configuration is handled in a `"../conf/settings.py"` file.
You can edit the file `/home/yunohost.app/django_example/local_settings.py` to enable or disable features.

Test sending emails, e.g.:

```bash
ssh admin@yourdomain.tld
root@yunohost:~# /home/yunohost.app/django_example/manage.py sendtestemail --admins
```

## Settings and upgrades

Almost everything related to Django Example's configuration is handled in a `"../conf/settings.py"` file.
You can edit the file `/home/yunohost.app/django_example/local_settings.py` to enable or disable features.

Test sending emails, e.g.:

```bash
ssh admin@yourdomain.tld
root@yunohost:~# /home/yunohost.app/django_example/manage.py sendtestemail --admins
```

How to debug a django YunoHost app, take a look into:

* https://github.com/YunoHost-Apps/django_example_ynh#developer-info


## local test

For quicker developing of django_example_ynh in the context of YunoHost app,
it's possible to run the Django developer server with the settings
and urls made for YunoHost installation.

e.g.:
```bash
~$ git clone https://github.com/YunoHost-Apps/django_example.git
~$ cd django_example_ynh/
~/django_example$ make
install-poetry         install or update poetry
install                install project via poetry
update                 update the sources and installation and generate "conf/requirements.txt"
lint                   Run code formatters and linter
fix-code-style         Fix code formatting
tox-listenvs           List all tox test environments
tox                    Run pytest via tox with all environments
pytest                 Run pytest
publish                Release new version to PyPi
local-test             Run local_test.py to run the project locally
local-diff-settings    Run "manage.py diffsettings" with local test

~/django_example$ make install-poetry
~/django_example$ make install
~/django_example$ make local-test
```

Notes:

* SQlite database will be used
* A super user with username `test` and password `test` is created
* The page is available under `http://127.0.0.1:8000/app_path/`


## history

* [compare v0.1.5...master](https://github.com/YunoHost-Apps/django_example/compare/v0.2.0...master) **dev**
  * tbc
* [v0.2.0 - 15.09.2021](https://github.com/YunoHost-Apps/django_example/compare/v0.1.5...v0.2.0)
  * rename/split `django_example_ynh` into:
    * [django_yunohost_integration](https://github.com/jedie/django_yunohost_integration) - Python package with the glue code to integrate a Django project with YunoHost
    * [django_example_ynh](https://github.com/YunoHost-Apps/django_example) - Demo YunoHost App to demonstrate the integration of a Django project under YunoHost
* [v0.1.5 - 19.01.2021](https://github.com/YunoHost-Apps/django_example/compare/v0.1.4...v0.1.5)
  * Make some deps `gunicorn`, `psycopg2-binary`, `django-redis`, `django-axes` optional
* [v0.1.4 - 08.01.2021](https://github.com/YunoHost-Apps/django_example/compare/v0.1.3...v0.1.4)
  * Bugfix [CSRF verification failed on POST requests #7](https://github.com/YunoHost-Apps/django_example/issues/7)
* [v0.1.3 - 08.01.2021](https://github.com/YunoHost-Apps/django_example/compare/v0.1.2...v0.1.3)
  * set "DEBUG = True" in local_test (so static files are served and auth works)
  * Bugfixes and cleanups
* [v0.1.2 - 29.12.2020](https://github.com/YunoHost-Apps/django_example/compare/v0.1.1...v0.1.2)
  * Bugfixes
* [v0.1.1 - 29.12.2020](https://github.com/YunoHost-Apps/django_example/compare/v0.1.0...v0.1.1)
  * Refactor "create_superuser" to a manage command, useable via "django_example_ynh" in `INSTALLED_APPS`
  * Generate "conf/requirements.txt" and use this file for install
  * rename own settings and urls (in `/conf/`)
* [v0.1.0 - 28.12.2020](https://github.com/YunoHost-Apps/django_example/compare/f578f14...v0.1.0)
  * first working state
* [23.12.2020](https://github.com/YunoHost-Apps/django_example/commit/f578f144a3a6d11d7044597c37d550d29c247773)
  * init the project


## Links

* Report a bug about this package: https://github.com/YunoHost-Apps/django_example
* YunoHost website: https://yunohost.org/
* PyPi package: https://pypi.org/project/django-ynh/

These projects used `django_example_ynh`:

* https://github.com/YunoHost-Apps/django_example
* https://github.com/YunoHost-Apps/django-for-runners_ynh

---

# Developer info

The App project will be stored under `__DATA_DIR__` (e.g.: `/home/yunohost.app/$app/`) that's Django's `settings.DATA_DIR_PATH`
"static" / "media" files to serve via nginx are under `__INSTALL_DIR__` (e.g.: `/var/www/$app/`) that's `settings.INSTALL_DIR_PATH`

## package installation / debugging

This app is not in YunoHost app catalog. Test install, e.g.:
```bash
~# git clone https://github.com/YunoHost-Apps/django_example_ynh.git
~# yunohost app install django_example_ynh/ -f
```
To update:
```bash
~# cd django_example_ynh
~/django_example_ynh# git fetch && git reset --hard origin/testing
~/django_example_ynh# yunohost app upgrade django_example -u . -F
```

To remove call e.g.:
```bash
sudo yunohost app remove django_example
```

Backup / remove / restore cycle, e.g.:
```bash
yunohost backup create --apps django_example
yunohost backup list
archives:
  - django_example_ynh-pre-upgrade1
  - 20230822-062848
yunohost app remove django_example
yunohost backup restore 20230822-062848 --apps django_example
```

Debug the installation, e.g.:
```bash
root@yunohost:~# cat /etc/yunohost/apps/django_example/settings.yml
...
app: django_example
...
data_dir: /home/yunohost.app/django_example
...
install_dir: /var/www/django_example
...
log_file: /var/log/django_example/django_example.log
...

root@yunohost:~# ls -la /var/www/django_example/
total 18
drwxr-xr-x 4 root root 4 Dec  8 08:36 .
drwxr-xr-x 6 root root 6 Dec  8 08:36 ..
drwxr-xr-x 2 root root 2 Dec  8 08:36 media
drwxr-xr-x 7 root root 8 Dec  8 08:40 static

root@yunohost:~# ls -la /home/yunohost.app/django_example/
total 58
drwxr-xr-x 5 django_example_ynh django_example_ynh   11 Dec  8 08:39 .
drwxr-xr-x 3 root        root           3 Dec  8 08:36 ..
-rw-r--r-- 1 django_example_ynh django_example_ynh  460 Dec  8 08:39 gunicorn.conf.py
-rw-r--r-- 1 django_example_ynh django_example_ynh    0 Dec  8 08:39 local_settings.py
-rwxr-xr-x 1 django_example_ynh django_example_ynh  274 Dec  8 08:39 manage.py
-rw-r--r-- 1 django_example_ynh django_example_ynh  171 Dec  8 08:39 secret.txt
drwxr-xr-x 6 django_example_ynh django_example_ynh    6 Dec  8 08:37 venv
-rw-r--r-- 1 django_example_ynh django_example_ynh  115 Dec  8 08:39 wsgi.py
-rw-r--r-- 1 django_example_ynh django_example_ynh 4737 Dec  8 08:39 django_example_ynh_demo_settings.py

root@yunohost:~# /home/yunohost.app/django_example/manage.py diffsettings
...
root@yunohost:~# /home/yunohost.app/django_example/manage.py check
ENV_TYPE:None
PROJECT_PATH:/home/yunohost.app/django_example/venv/lib/python3.9/site-packages
BASE_PATH:/root/django_example
System check identified no issues (0 silenced).

root@yunohost:~# cat /etc/systemd/system/django_example.service
...

root@yunohost:~# systemctl reload-or-restart django_example
root@yunohost:~# journalctl --unit=django_example --follow
...
root@yunohost:~# tail -f /var/log/django_example/django_example.log
...
root@yunohost:~# tail -f /var/log/nginx/*.log
...

root@yunohost:~# ls -la /etc/nginx/conf.d/
root@yunohost:~# cat /etc/nginx/conf.d/$domain.d/django_example.conf
```
