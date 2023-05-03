import sqlite3 as sql


def read_data(table_name):
    con = sql.connect("C:\\Users\\santosh.a.d.kulkarni\\PycharmProjects\\PRtool_alphav1\\entities\\instance\\isr_database.db")
    cur = con.cursor()

    read_query = "SELECT * FROM " + table_name
    cur.execute(read_query)
    users = cur.fetchall()
    print(users)
    con.close()


if __name__ == '__main__':
    read_data("isr_new_issue")
