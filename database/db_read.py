import sqlite3 as sql
from parser import config_parser


def read_data(table_name):
    con = sql.connect(config_parser.db_hostname)
    cur = con.cursor()

    read_query = "SELECT * FROM " + table_name
    cur.execute(read_query)
    users = cur.fetchall()
    print(users)
    con.close()


if __name__ == '__main__':
    read_data("isr_registered_users")
