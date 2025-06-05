import os;
from get_db_list import get_db_list;
from backup_database import backup_database;
from remote_backup import remote_upload_backup, remote_cleanup_old_backups;
from local_backup import local_save_backup, local_cleanup_old_backups;
from dotenv import load_dotenv;
from util_functions import str2bool;
from send_email_notifaction import send_email_notification;
# Load environment variables
load_dotenv()

# Configuration from .env
DO_REMOTE_BACKUP = str2bool(os.getenv("DO_REMOTE_BACKUP", "True"))
DO_LOCAL_BACKUP = str2bool(os.getenv("DO_LOCAL_BACKUP", "True"))
DO_EMAIL_NOTIFICATION = str2bool(os.getenv("DO_EMAIL_NOTIFICATION", "True"))


def main():
    db_list = get_db_list()
    backup_status = {}
    summary = ""

    for db in db_list:
        
        try:
            temp_file = backup_database(db)
            if DO_REMOTE_BACKUP:
                remote_upload_backup(temp_file)
                remote_cleanup_old_backups(db)

            if DO_LOCAL_BACKUP:
                local_save_backup(temp_file)
                local_cleanup_old_backups(db)

            backup_status[db] = "Success"
            os.remove(temp_file)
        except Exception as e:
            backup_status[db] = f"Failed: {str(e)}"
    print("Backup Status:")
    for db, status in backup_status.items():
        print(f"{db}: {status}")
    if DO_EMAIL_NOTIFICATION:
        summary = "\n".join([f"{db}: {status}" for db, status in backup_status.items()])
        body = f"Hello,\n\nHere is the backup status for today:\n\n{summary}\n\nRegards,\nBackup Bot"
        send_email_notification(body)


if __name__ == "__main__":
    main()
