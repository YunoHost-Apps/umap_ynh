#!/bin/bash

#=================================================
# RETRIEVE ARGUMENTS FROM THE MANIFEST
#=================================================

# Transfer the main SSO domain to the App:
ynh_current_host=$(cat /etc/yunohost/current_host)

umap_with_extra_deps="umap-project[yunohost,sync]"

#=================================================
# SET CONSTANTS
#=================================================

# e.g.: point pip cache to: /home/yunohost.app/$app/.cache/
XDG_CACHE_HOME="$data_dir/.cache/"

#=================================================
# HELPERS
#=================================================

myynh_fix_file_permissions() {
    # /var/www/$app/
    # static files served by nginx, so use www-data group:
    chown -c -R "$app:www-data" "$install_dir"
    # TODO: forbid write access to $app for the install_dir
    chmod -c u+rwx,g+rx,o-rwx "$install_dir"
    # TODO: give read/write access to local_settings.py only to root
    # and give read-only access to $app (or www-data?) so they can read it.

    # /home/yunohost.app/$app/
    chown -c -R "$app:$app" "$data_dir"
    chmod -c u+rwx,g+rwx,o-rwx "$data_dir"
}
