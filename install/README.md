# Install a Ubuntu System
## Create a bootable startup disk
- Dash > __Startup Disk Creator__.

## Run in Terminal
```bash
sudo ~/Desktop/data/hub/install/ubuntu
```

## Copy SSH public key to GitHub

## Change Git repository remote name
```text
3. Set your remote URL to a form that supports SSH 1

If you have done the steps above and are still getting the password prompt, make sure your repo URL is in the form

git+ssh://git@github.com/username/reponame.git
as opposed to

https://github.com/username/reponame.git
To see your repo URL, run:

git remote show origin
You can change the URL with:

git remote set-url origin git+ssh://git@github.com/username/reponame.git
```

## Config Jupyter - Do this before install jupyter
```text
jupyter notebook --generate-config
```
```python3
from notebook.auth import passwd
passwd()
```
- Copy the password starting 'sha1:...' in jupyter_notebook_config.py
- c.NotebookApp.password = 'sha1:...'
- c.NotebookApp.certfile = 
- c.NotebookApp.keyfile = 
```bash
crontab -r
crontab ~/Desktop/data/hub/crontab/cronjobs
crontab -l
```
