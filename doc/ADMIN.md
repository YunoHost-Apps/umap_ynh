# Settings

Almost everything related to Umap's configuration is handled in a `"__INSTALL_DIR__/conf/settings.py"` file. You should not edit this file manually, otherwise your changes will be overwritten.
You can insteaad edit the file `__INSTALL_DIR__/local_settings.py` to enable or disable features.

## Testing the emails are sent

You may log in Yunohost using ssh and run the following command:

```bash
root@yunohost:~# /home/yunohost.app/umap/manage.py sendtestemail --admins
```

## Debugging Umap

Take a look into:

* https://github.com/YunoHost-Apps/umap_ynh#developer-info
