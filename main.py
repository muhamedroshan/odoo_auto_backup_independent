import os;
from get_db_list import get_db_list;
from backup_database import backup_database;
from remote_backup import remote_upload_backup, remote_cleanup_old_backups;
from local_backup import local_save_backup, local_cleanup_old_backups;
from dotenv import load_dotenv;
from util_functions import str2bool;

# Load environment variables
load_dotenv()

# Configuration from .env
DO_REMOTE_BACKUP = str2bool(os.getenv("DO_REMOTE_BACKUP", "True"))
DO_LOCAL_BACKUP = str2bool(os.getenv("DO_LOCAL_BACKUP", "True"))


def main():
    db_list = get_db_list()
    for db in db_list:

        print(db)

        temp_file = backup_database(db)
        print(temp_file)


        if DO_REMOTE_BACKUP:
            print("Uploading to remote server...")
            
        if DO_LOCAL_BACKUP:
            print("Saving to local storage...")

        #delete temp file
        os.remove(temp_file)


if __name__ == "__main__":
    main()
