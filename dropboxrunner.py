#!/usr/bin/env python

# Part of the code derived from
# https://wiki.archlinux.org/index.php/Dropbox#Multiple_Dropbox_Instances
import json
import os
import subprocess
import shlex


user_home = os.environ.get('HOME')
default_xdg_config_home = os.path.join(user_home, '.config')
xdg_config_home = os.environ.get('XDG_CONFIG_HOME', default_xdg_config_home)

config_name = 'dropboxes'
config_dir = xdg_config_home
config_path = os.path.join(config_dir, config_name)


os.makedirs(config_dir, exist_ok=True)

# Non-race touch
fd = os.open(config_path, os.O_APPEND, mode=0o644)
if os.utime in os.supports_fd:
    path_or_fd = fd
else:
    path_or_fd = config_path
os.utime(path_or_fd)
os.close(fd)


with open(config_path) as config_f:
    config = json.load(config_f)

default_dbox_install_dir = os.path.join(user_home, '.dropbox-dist')
dbox_install_dir = config.get('dbox_install_dir', default_dbox_install_dir)
dropboxes = config.get('dropboxes', [])
dboxd_bin_path = os.path.join(dbox_install_dir, 'dropboxd')
dbox_cmd = shlex.split('{} start -i'.format(dboxd_bin_path))
dbox_env = os.environ.copy()

for dbox in dropboxes:
    os.makedirs(dbox, exist_ok=True)
    for needed_file in ('.gtkrc-2.0', '.Xauthority'):
        try:
            os.symlink(os.path.join(user_home, needed_file),
                    os.path.join(dbox, needed_file))
        except FileExistsError:
            pass
    dbox_env['HOME'] = dbox
    subprocess.Popen(dbox_cmd, env=dbox_env)
