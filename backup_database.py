import xmlrpc.client
import os
import datetime
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from .env
ODOO_URL = os.getenv("ODOO_URL")
ODOO_PORT = int(os.getenv("ODOO_PORT"))
ODOO_MASTER_PASSWORD = os.getenv("ODOO_MASTER_PASSWORD")
LOCAL_BACKUP_DIR = os.getenv("LOCAL_BACKUP_DIR")



def backup_database(db_name):

    os.makedirs(LOCAL_BACKUP_DIR, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"{db_name}_{timestamp}.zip"
    backup_path = os.path.join(LOCAL_BACKUP_DIR, backup_file)

    db = xmlrpc.client.ServerProxy(f"{ODOO_URL}:{ODOO_PORT}/xmlrpc/db")
    backup_data = db.dump(ODOO_MASTER_PASSWORD, db_name, 'zip')

    with open(backup_path, 'wb') as f:
        f.write(base64.b64decode(backup_data))

    return backup_path