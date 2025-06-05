import os
import shutil
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from .env
LOCAL_BACKUP_DIR = os.getenv("LOCAL_BACKUP_DIR", "/opt/odoo_backups/")

def local_save_backup(temp_path):
    shutil.copy2(temp_path, os.path.join(LOCAL_BACKUP_DIR, os.path.basename(temp_path)))
    return True


def local_cleanup_old_backups(prefix):
    files = sorted([
        f for f in os.listdir(LOCAL_BACKUP_DIR)
        if f.startswith(prefix) and f.endswith(".zip")
    ], reverse=True)

    for f in files[4:]:  # Keep latest 4
        os.remove(os.path.join(LOCAL_BACKUP_DIR, f))