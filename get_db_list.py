import xmlrpc.client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration from .env
ODOO_URL = os.getenv("ODOO_URL")
ODOO_PORT = int(os.getenv("ODOO_PORT"))
ODOO_MASTER_PASSWORD = os.getenv("ODOO_MASTER_PASSWORD")

def get_db_list():
    common = xmlrpc.client.ServerProxy(f"{ODOO_URL}:{ODOO_PORT}/xmlrpc/2/common")
    return common.list_databases()