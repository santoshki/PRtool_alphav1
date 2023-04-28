import sqlite3


def create_table(table_name):
    try:
        connection_db = sqlite3.connect("pr_database.db")
        cursor_obj = connection_db.cursor()
        query = "CREATE TABLE " + str(table_name) + "(id INTEGER PRIMARY KEY AUTOINCREMENT,first_name VARCHAR(255), " \
                                                    "last_name VARCHAR(255),username VARCHAR(255), email " \
                                                    "VARCHAR(255), password VARCHAR(255)); "
        cursor_obj.execute(query)
        print("Table created successfully!")
        cursor_obj.close()
        connection_db.commit()
    except Exception as e:
        print("Exception occurred while creating table in db", e)


if __name__ == '__main__':
    create_table("pr_registered_users")
