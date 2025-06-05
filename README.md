# Python program that run indepently outside odoo to create automatic backups
To achieve independent automated weekly backups of your Odoo databases and store them on another server or locally, while retaining the last 4 weeks of backups

## How to setup

- ### step 1
 
clone repository
```
git clone https://github.com/muhamedroshan/odoo_auto_backup_independent.git
```
- ### step 2

install requirements
```
pip3 install -r requirements.txt
```

- ### step 3

configure environmental variable
it is mandatory to provide **odoo configuration variable**

| Variable | Expected Values |
|----------|-----------------|
| ODOO_URL | provide URL of odoo db hosted server example "http://server" |
| ODOO_PORT | port number of server where odoo is hosted exampl "8069" |
| ODOO_MASTER_PASSWORD | your master password |
| TEMP_LOCAL_BACKUP_DIR | temporary location to store backup file temporary |

configure functions such as **email notification, local save or not, remote transfer or not**

| Variable | Values |
|----------|--------|
| DO_REMOTE_BACKUP | `True` if need enable remote backup else `False` |
| DO_LOCAL_BACKUP | `True` if need enable local backup else `False` |
| DO_EMAIL_NOTIFICATION | `True` if need enable email notification else `False` |

**Note : If any functions enabled it is mandatory to provide corressponding configuration details for such functions**

- ### step 4

try test run from terminal
```
python3 main.py
```
- ### step 5

Automate with Cron
Edit crontab with:
```bash
crontab -e
```
Add this line to run the script every Sunday at midnight:
```
0 0 * * 0 /usr/bin/python3 /path/to/your/script.py >> /var/log/odoo_backup.log 2>&1

```
