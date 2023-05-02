import sqlite3 as sql


def db_delete_table(table_name):
    try:
        connection = sql.connect("E:\\Entreprenuership\\PycharmProjects\\PRtool_alphav1\\entities\\isr_database.db")
        query = "DROP TABLE " + str(table_name)
        connection.execute(query)
        print("Table dropped from the db.")
        connection.commit()
        connection.close()
    except Exception as e:
        print("Exception occurred while dropping the table in the db", e)


if __name__ == '__main__':
    db_delete_table("isr_new_issue")