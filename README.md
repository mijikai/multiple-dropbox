Run multiple dropboxes for different accounts. This would be useful for people
that separates data for home or work.

In order for this to work, each dropbox instance is run with different HOME
variable. To add an instance, create or edit the file
`$XDG_CONFIG_HOME/dropboxes` (`XDG_CONFIG_HOME` is usually `$HOME/.config`),
add a `dropboxes` and put the path to new dropbox home. If your dropbox
installation is located other than `$HOME/.dropbox-dist`, add
`dbox_install_dir` with the path to your dropbox installation as its value.

An example configuration will be:
```json
{
    "dbox_install_dir": "/opt/dropbox/",
    "dropboxes": [
        "/path/to/one/dbox",
        "/path/to/another"
    ]
}
```
Run dropboxrunner.sh and popup(s) will appear asking to login or create a new
account. Enter the credentials for each instance and your ready to go.
