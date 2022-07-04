# Broadcast Reddit DMs

### Create Python3 virtual environment for this folder

> $ python3 -m venv venv
> $ . venv/bin/activate

*NOTE: above will work with MacOSX/Linux environment windows might be slightly different*

### install dependencies
_You should be in the virtual environment (venv)_

> (venv) pip install -r requirements.txt

### update config.yaml

client_id and client_secret values can be obtained by creating a 'script' app here (while logged into whichever user you want to send messages from)

https://www.reddit.com/prefs/apps

just add the users in the mass DM list under recipients

### run from venv

> (venv) python broadcast_dm.py