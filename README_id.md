<!--
N.B.: README ini dibuat secara otomatis oleh <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Ini TIDAK boleh diedit dengan tangan.
-->

# Django Example untuk YunoHost

[![Tingkat integrasi](https://dash.yunohost.org/integration/django_example.svg)](https://ci-apps.yunohost.org/ci/apps/django_example/) ![Status kerja](https://ci-apps.yunohost.org/ci/badges/django_example.status.svg) ![Status pemeliharaan](https://ci-apps.yunohost.org/ci/badges/django_example.maintain.svg)

[![Pasang Django Example dengan YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django_example)

*[Baca README ini dengan bahasa yang lain.](./ALL_README.md)*

> *Paket ini memperbolehkan Anda untuk memasang Django Example secara cepat dan mudah pada server YunoHost.*
> *Bila Anda tidak mempunyai YunoHost, silakan berkonsultasi dengan [panduan](https://yunohost.org/install) untuk mempelajari bagaimana untuk memasangnya.*

## Ringkasan

[![tests](https://github.com/YunoHost-Apps/django_example_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django_example_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/django_example_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/django_example_ynh)
[![django_example_ynh @ PyPi](https://img.shields.io/pypi/v/django_example_ynh?label=django_example_ynh%20%40%20PyPi)](https://pypi.org/project/django_example_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/django_example_ynh)](https://github.com/YunoHost-Apps/django_example_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/django_example_ynh)](https://github.com/YunoHost-Apps/django_example_ynh/blob/main/LICENSE)

Demo YunoHost Application to demonstrate the integration of a Django project under YunoHost.

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Versi terkirim:** 0.2.0~ynh4
## Dokumentasi dan sumber daya

- Depot kode aplikasi hulu: <https://github.com/jedie/django-example>
- Gudang YunoHost: <https://apps.yunohost.org/app/django_example>
- Laporkan bug: <https://github.com/YunoHost-Apps/django_example_ynh/issues>

## Info developer

Silakan kirim pull request ke [`testing` branch](https://github.com/YunoHost-Apps/django_example_ynh/tree/testing).

Untuk mencoba branch `testing`, silakan dilanjutkan seperti:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django_example_ynh/tree/testing --debug
atau
sudo yunohost app upgrade django_example -u https://github.com/YunoHost-Apps/django_example_ynh/tree/testing --debug
```

**Info lebih lanjut mengenai pemaketan aplikasi:** <https://yunohost.org/packaging_apps>
