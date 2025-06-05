import os
import paramiko
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from .env
REMOTE_HOST = os.getenv("REMOTE_HOST")
REMOTE_PORT = os.getenv("REMOTE_PORT")
REMOTE_USERNAME = os.getenv("REMOTE_USERNAME")
REMOTE_PASSWORD = os.getenv("REMOTE_PASSWORD")
REMOTE_BACKUP_DIR = os.getenv("REMOTE_BACKUP_DIR", "/opt/odoo_backups/")

def remote_upload_backup(local_path):
    transport = paramiko.Transport((REMOTE_HOST, int(REMOTE_PORT)))
    transport.connect(username=REMOTE_USERNAME, password=REMOTE_PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        sftp.chdir(REMOTE_BACKUP_DIR)
    except IOError:
        sftp.mkdir(REMOTE_BACKUP_DIR)
        sftp.chdir(REMOTE_BACKUP_DIR)

    filename = os.path.basename(local_path)
    sftp.put(local_path, os.path.join(REMOTE_BACKUP_DIR, filename))
    sftp.close()
    transport.close()

def remote_cleanup_old_backups(prefix):
    transport = paramiko.Transport((REMOTE_HOST, int(REMOTE_PORT)))
    transport.connect(username=REMOTE_USERNAME, password=REMOTE_PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        sftp.chdir(REMOTE_BACKUP_DIR)
    except IOError:
        print("Remote path not found.")
        sftp.close()
        transport.close()
        return

    files = sorted(
        [f for f in sftp.listdir() if f.startswith(prefix)],
        reverse=True
    )

    for f in files[4:]:
        sftp.remove(os.path.join(REMOTE_BACKUP_DIR, f))

    sftp.close()
    transport.close()