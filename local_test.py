#!/usr/bin/env python3

"""
    Start django_ynh in YunoHost setup locally.

    Run via:
        make local-test

    see README for details ;)
"""
import base64
import os
import shlex
import subprocess
import sys
from pathlib import Path


os.environ['DJANGO_SETTINGS_MODULE'] = 'django_ynh_demo_settings'

try:
    import django_ynh  # noqa
except ImportError as err:
    raise ImportError('Couldn\'t import django_ynh. Did you ' 'forget to activate a virtual environment?') from err


BASE_PATH = Path(__file__).parent.absolute()
TEST_PATH = BASE_PATH / 'local_test'
CONF_PATH = BASE_PATH / 'conf'

FINAL_HOME_PATH = TEST_PATH / 'opt_yunohost'
FINAL_WWW_PATH = TEST_PATH / 'var_www'
LOG_FILE = TEST_PATH / 'var_log_django_ynh.log'

MANAGE_PY_FILE = CONF_PATH / 'manage.py'
SETTINGS_FILE = CONF_PATH / 'django_ynh_demo_settings.py'
URLS_FILE = CONF_PATH / 'django_ynh_demo_urls.py'

REPLACES = {
    '__FINAL_HOME_PATH__': str(FINAL_HOME_PATH),
    '__FINAL_WWW_PATH__': str(FINAL_WWW_PATH),
    '__LOG_FILE__': str(TEST_PATH / 'var_log_django_ynh.log'),
    '__PATH_URL__': 'app_path',
    '__DOMAIN__': '127.0.0.1',
    'django.db.backends.postgresql': 'django.db.backends.sqlite3',
    "'NAME': '__APP__',": f"'NAME': '{TEST_PATH / 'test_db.sqlite'}',",
    'django_redis.cache.RedisCache': 'django.core.cache.backends.dummy.DummyCache',

    # Just use the default logging setup from django_ynh project:
    'LOGGING = {': 'HACKED_DEACTIVATED_LOGGING = {',
}


def verbose_check_call(command, verbose=True, **kwargs):
    """ 'verbose' version of subprocess.check_call() """
    if verbose:
        print('_' * 100)
        msg = f'Call: {command!r}'
        verbose_kwargs = ', '.join(f'{k}={v!r}' for k, v in sorted(kwargs.items()))
        if verbose_kwargs:
            msg += f' (kwargs: {verbose_kwargs})'
        print(f'{msg}\n', flush=True)

    env = os.environ.copy()
    env['PYTHONUNBUFFERED'] = '1'

    popenargs = shlex.split(command)
    subprocess.check_call(popenargs, universal_newlines=True, env=env, **kwargs)


def call_manage_py(args):
    verbose_check_call(
        command=f'{sys.executable} manage.py {args}',
        cwd=FINAL_HOME_PATH,
    )


def copy_patch(src_file, replaces=None):
    dst_file = FINAL_HOME_PATH / src_file.name
    print(f'{src_file.relative_to(BASE_PATH)} -> {dst_file.relative_to(BASE_PATH)}')

    with src_file.open('r') as f:
        content = f.read()

    if replaces:
        for old, new in replaces.items():
            content = content.replace(old, new)

    with dst_file.open('w') as f:
        f.write(content)


def assert_is_dir(dir_path):
    assert dir_path.is_dir, f'Directory does not exists: {dir_path}'


def assert_is_file(file_path):
    assert file_path.is_file, f'File not found: {file_path}'


def main():
    print('-' * 100)

    assert_is_dir(BASE_PATH)
    assert_is_dir(CONF_PATH)
    assert_is_file(SETTINGS_FILE)
    assert_is_file(URLS_FILE)

    for p in (TEST_PATH, FINAL_HOME_PATH, FINAL_WWW_PATH):
        if p.is_dir():
            print(f'Already exists: "{p.relative_to(BASE_PATH)}", ok.')
        else:
            print(f'Create: "{p.relative_to(BASE_PATH)}"')
            p.mkdir(parents=True, exist_ok=True)

    LOG_FILE.touch(exist_ok=True)

    # conf/manage.py -> local_test/manage.py
    copy_patch(src_file=MANAGE_PY_FILE)

    # conf/django_ynh_demo_settings.py -> local_test/django_ynh_demo_settings.py
    copy_patch(src_file=SETTINGS_FILE, replaces=REPLACES)

    # conf/ynh_urls.py -> local_test/ynh_urls.py
    copy_patch(src_file=URLS_FILE, replaces=REPLACES)

    with Path(FINAL_HOME_PATH / 'local_settings.py').open('w') as f:
        f.write('# Only for local test run\n')
        f.write('SERVE_FILES = True  # used in src/inventory_project/urls.py\n')
        f.write('AUTH_PASSWORD_VALIDATORS = []  # accept all passwords\n')

    # call "local_test/manage.py" via subprocess:
    call_manage_py('check --deploy')
    call_manage_py('migrate --no-input')
    call_manage_py('collectstatic --no-input')

    verbose_check_call(
        command=(
            f'{sys.executable} -m django_ynh.create_superuser'
            ' --ds="django_ynh_demo_settings" --username="test" --password="test"'
        ),
        cwd=FINAL_HOME_PATH,
    )

    # All environment variables are passed to Django's "runnserver" ;)
    # "Simulate" SSOwat authentication, by set "http headers"
    # Still missing is the 'SSOwAuthUser' cookie,
    # but this is ignored, if settings.DEBUG=True ;)
    os.environ['HTTP_AUTH_USER'] = 'test'
    os.environ['HTTP_REMOTE_USER'] = 'test'

    creds = str(base64.b64encode(b'test:test'), encoding='utf-8')
    basic_auth = f'basic {creds}'
    os.environ['HTTP_AUTHORIZATION'] = basic_auth

    try:
        call_manage_py('runserver --nostatic')
    except KeyboardInterrupt:
        print('\nBye ;)')


if __name__ == '__main__':
    main()
