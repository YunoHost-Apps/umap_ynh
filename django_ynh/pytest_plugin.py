import os
import sys
from pathlib import Path

import pytest

from django_ynh.path_utils import assert_is_dir, assert_is_file


def pytest_addoption(parser):
    group = parser.getgroup("django_ynh")
    group.addoption(
        "--django_settings_path",
        action="store",
        metavar="path",
        help='Path to YunoHost package settings.py file (in "conf" directory)',
    )


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(early_config, parser, args):
    base_path = Path(__file__).parent.parent

    local_test = Path(base_path / 'local_test')
    assert_is_dir(local_test)

    local_test_opt_yunohost = Path(local_test / 'opt_yunohost')
    assert_is_dir(local_test_opt_yunohost)

    assert_is_file(local_test_opt_yunohost / 'django_ynh_demo_settings.py')

    sys.path.insert(0, str(local_test_opt_yunohost))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_ynh_demo_settings'

    # print(1111111111111, early_config) # _pytest.config.Config
    # print(22222, parser) # _pytest.config.argparsing.Parser
    # print(3333, args) # ['--import-mode=importlib', '--reuse-db', '--nomigrations', '--cov=.', '--cov-report', 'term-missing', '--cov-report', 'html', '--cov-report', 'xml', '--no-cov-on-fail', '--showlocals', '--doctest-modules', '--failed-first', '--last-failed-no-failures', 'all', '--new-first', '-p', 'django_ynh.pytest_plugin', '-x', '--trace-config']
    #
    # options = parser.parse_known_args(args)
    # if options.version or options.help:
    #     return
    #
    # conf_path = options.conf_path
    #
    # raise RuntimeError(f'{conf_path}')
