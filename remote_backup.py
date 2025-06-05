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

def remote_upload_backup(local_path, remote_path):
    transport = paramiko.Transport((REMOTE_HOST, REMOTE_PORT))
    transport.connect(username=REMOTE_USERNAME, password=REMOTE_PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        sftp.chdir(remote_path)
    except IOError:
        sftp.mkdir(remote_path)
        sftp.chdir(remote_path)

    filename = os.path.basename(local_path)
    sftp.put(local_path, os.path.join(remote_path, filename))
    sftp.close()
    transport.close()

def remote_cleanup_old_backups(remote_path, prefix):
    transport = paramiko.Transport((REMOTE_HOST, REMOTE_PORT))
    transport.connect(username=REMOTE_USERNAME, password=REMOTE_PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        sftp.chdir(remote_path)
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
        sftp.remove(os.path.join(remote_path, f))

    sftp.close()
    transport.close()