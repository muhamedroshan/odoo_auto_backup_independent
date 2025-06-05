import xmlrpc.client

def get_db_list():
    common = xmlrpc.client.ServerProxy(f"{ODOO_URL}:{ODOO_PORT}/xmlrpc/2/common")
    return common.list_databases()