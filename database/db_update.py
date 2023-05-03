import sqlite3 as sql
from parser import config_parser


def db_delete_table(table_name):
    try:
        connection = sql.connect(config_parser.db_hostname)
        query = "DROP TABLE " + str(table_name)
        connection.execute(query)
        print("Table dropped from the db.")
        connection.commit()
        connection.close()
    except Exception as e:
        print("Exception occurred while dropping the table in the db", e)


if __name__ == '__main__':
    db_delete_table("isr_new_issue")
