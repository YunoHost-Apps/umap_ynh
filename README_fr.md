<!--
Nota bene : ce README est automatiquement généré par <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Il NE doit PAS être modifié à la main.
-->

# Django Example pour YunoHost

[![Niveau d’intégration](https://apps.yunohost.org/badge/integration/django_example)](https://ci-apps.yunohost.org/ci/apps/django_example/)
![Statut du fonctionnement](https://apps.yunohost.org/badge/state/django_example)
![Statut de maintenance](https://apps.yunohost.org/badge/maintained/django_example)

[![Installer Django Example avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=django_example)

*[Lire le README dans d'autres langues.](./ALL_README.md)*

> *Ce package vous permet d’installer Django Example rapidement et simplement sur un serveur YunoHost.*
> *Si vous n’avez pas YunoHost, consultez [ce guide](https://yunohost.org/install) pour savoir comment l’installer et en profiter.*

## Vue d’ensemble

[![tests](https://github.com/YunoHost-Apps/django_example_ynh/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/YunoHost-Apps/django_example_ynh/actions/workflows/tests.yml)
[![codecov](https://codecov.io/github/jedie/django_example_ynh/branch/main/graph/badge.svg)](https://app.codecov.io/github/jedie/django_example_ynh)
[![django_example_ynh @ PyPi](https://img.shields.io/pypi/v/django_example_ynh?label=django_example_ynh%20%40%20PyPi)](https://pypi.org/project/django_example_ynh/)
[![Python Versions](https://img.shields.io/pypi/pyversions/django_example_ynh)](https://github.com/YunoHost-Apps/django_example_ynh/blob/main/pyproject.toml)
[![License GPL-3.0-or-later](https://img.shields.io/pypi/l/django_example_ynh)](https://github.com/YunoHost-Apps/django_example_ynh/blob/main/LICENSE)

Demo YunoHost Application to demonstrate the integration of a Django project under YunoHost.

Pull requests welcome ;)

This package for YunoHost used [django-yunohost-integration](https://github.com/YunoHost-Apps/django_yunohost_integration)


**Version incluse :** 0.2.0~ynh4
## Documentations et ressources

- Dépôt de code officiel de l’app : <https://github.com/jedie/django-example>
- YunoHost Store : <https://apps.yunohost.org/app/django_example>
- Signaler un bug : <https://github.com/YunoHost-Apps/django_example_ynh/issues>

## Informations pour les développeurs

Merci de faire vos pull request sur la [branche `testing`](https://github.com/YunoHost-Apps/django_example_ynh/tree/testing).

Pour essayer la branche `testing`, procédez comme suit :

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/django_example_ynh/tree/testing --debug
ou
sudo yunohost app upgrade django_example -u https://github.com/YunoHost-Apps/django_example_ynh/tree/testing --debug
```

**Plus d’infos sur le packaging d’applications :** <https://yunohost.org/packaging_apps>
