import os
import shutil
import subprocess
from pathlib import Path

import tomli
from django_tools.unittest_utils.project_setup import check_editor_config

import django_yunohost_integration


PACKAGE_ROOT = Path(__file__).parent.parent


def assert_file_contains_string(file_path, string):
    with file_path.open('r') as f:
        for line in f:
            if string in line:
                return
    raise AssertionError(f'File {file_path} does not contain {string!r} !')


def test_version():
    upstream_version = django_yunohost_integration.__version__

    pyproject_toml_path = Path(PACKAGE_ROOT, 'pyproject.toml')
    pyproject_toml = tomli.loads(pyproject_toml_path.read_text(encoding='UTF-8'))
    pyproject_version = pyproject_toml['tool']['poetry']['version']
    assert pyproject_version.startswith(f'{upstream_version}+ynh')

    # pyproject.toml needs a PEP 440 conform version and used "+ynh"
    # the YunoHost syntax is: "~ynh", just "convert this:
    manifest_version = pyproject_version.replace('+', '~')

    assert_file_contains_string(
        file_path=Path(PACKAGE_ROOT, 'manifest.json'),
        string=f'"version": "{manifest_version}"',
    )


def test_poetry_check():
    poerty_bin = shutil.which('poetry')

    output = subprocess.check_output(
        [poerty_bin, 'check'],
        text=True,
        env=os.environ,
        stderr=subprocess.STDOUT,
        cwd=str(PACKAGE_ROOT),
    )
    print(output)
    assert output == 'All set!\n'


def test_check_editor_config():
    check_editor_config(package_root=PACKAGE_ROOT)
