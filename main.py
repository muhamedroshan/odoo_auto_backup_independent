import os;
from get_db_list import get_db_list;

def main():
    db_list = get_db_list()
    for db in db_list:
        print(db)

if __name__ == "__main__":
    main()
