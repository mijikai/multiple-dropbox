Run multiple dropboxes for different accounts. This would be useful for people
that separates data for home or work.

In order for this to work, each dropbox instance is run with different HOME
variable. To add an instance, add a path to
`$XDG_CONFIG_HOME/dropboxes/dbox_lcoation` (`XDG_CONFIG_HOME` is usually
`$HOME/.config`) one line each and then run dropboxrunner.sh. Popup(s) will
appear asking to login or create a new account. Enter the credentials for each
instance and your ready to go.
