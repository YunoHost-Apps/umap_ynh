import os
import shutil
import subprocess
from pathlib import Path

import django_ynh


PACKAGE_ROOT = Path(django_ynh.__file__).parent.parent


def assert_file_contains_string(file_path, string):
    with file_path.open('r') as f:
        for line in f:
            if string in line:
                return
    raise AssertionError(f'File {file_path} does not contain {string!r} !')


def test_version(package_root=None, version=None):
    if package_root is None:
        package_root = PACKAGE_ROOT

    if version is None:
        version = django_ynh.__version__

    if 'dev' not in version and 'rc' not in version:
        version_string = f'v{version}'

        assert_file_contains_string(file_path=Path(package_root, 'README.md'), string=version_string)

    assert_file_contains_string(file_path=Path(package_root, 'pyproject.toml'), string=f'version = "{version}"')
    assert_file_contains_string(file_path=Path(package_root, 'manifest.json'), string=f'"version": "{version}~ynh",')

    assert_file_contains_string(
        file_path=Path(package_root, 'deployment', 'project.env'), string=f'PROJECT_VERSION={version}'
    )


def test_poetry_check(package_root=None):
    if package_root is None:
        package_root = PACKAGE_ROOT

    poerty_bin = shutil.which('poetry')

    output = subprocess.check_output(
        [poerty_bin, 'check'],
        universal_newlines=True,
        env=os.environ,
        stderr=subprocess.STDOUT,
        cwd=str(package_root),
    )
    print(output)
    assert output == 'All set!\n'
