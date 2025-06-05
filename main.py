import os;
from get_db_list import get_db_list;
from backup_database import backup_database;

def main():
    db_list = get_db_list()
    for db in db_list:
        print(db)
        path = backup_database(db)
        print(path)


if __name__ == "__main__":
    main()
