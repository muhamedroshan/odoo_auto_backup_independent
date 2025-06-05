import os
from backup_utils import get_db_list, backup_database, upload_backup, cleanup_old_backups, REMOTE_BACKUP_PATH

def main():
    db_list = get_db_list()
    for db in db_list:
        print(db)

if __name__ == "__main__":
    main()
