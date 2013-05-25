#!/bin/bash

# Part of the code copied from
# https://wiki.archlinux.org/index.php/Dropbox#Multiple_Dropbox_Instances

#*******************************                                                                        
# Multiple dropbox instances                                                                            
#*******************************                                                                        
                                                                                                        
: ${XDG_CONFIG_HOME:="$HOME/.config"}
dropbox_mul_config=dropboxes
dboxes_dir_config="$XDG_CONFIG_HOME/$dropbox_mul_config"

mkdir -p "$dboxes_dir_config"
touch -a "$dboxes_dir_config/dbox_location"
cat "$dboxes_dir_config/dbox_location" | while read dropbox;
do                                                                                                      
    if ! [ -d "$dropbox" ];then                                                                     
        mkdir "$dropbox"                                                                            
        ln -s "$HOME/.Xauthority" "$dropbox/.Xauthority"
    fi                                                                                                  
    HOME="$dropbox/" dropboxd start -i
done  
