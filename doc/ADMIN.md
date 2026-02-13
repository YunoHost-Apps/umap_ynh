## Settings and upgrades

Almost everything related to Django Example's configuration is handled in a `"../conf/settings.py"` file.
You can edit the file `__DATA_DIR__/local_settings.py` to enable or disable features.

Test sending emails, e.g.:

```bash
ssh admin@yourdomain.tld
root@yunohost:~# __DATA_DIR__/manage.py sendtestemail --admins
```

How to debug a django YunoHost app, take a look into:

* https://github.com/YunoHost-Apps/umap_ynh#developer-info
