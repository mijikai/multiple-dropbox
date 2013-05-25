#!/bin/bash

# Part of the code copied from
# https://wiki.archlinux.org/index.php/Dropbox#Multiple_Dropbox_Instances

#*******************************                                                                        
# Multiple dropbox instances                                                                            
#*******************************                                                                        

dropboxes=(.dropbox-personal .dropbox-work)                                                            

for dropbox in ${dropboxes[@]}                                                                          
do                                                                                                      
    if ! [ -d $HOME/$dropbox ];then                                                                     
        mkdir $HOME/$dropbox                                                                            
    fi                                                                                                  
    HOME=$HOME/$dropbox/ /usr/bin/dropbox start -i                                                      
done  
