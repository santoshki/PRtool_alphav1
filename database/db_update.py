import sqlite3 as sql
from parser import config_parser
from werkzeug.security import generate_password_hash, check_password_hash


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


def change_password(email_id):
    pass


def reset_password(email_id):
    try:
        connection = sql.connect(config_parser.db_hostname)
        connection_cursor = connection.cursor()
        hashed_password = generate_password_hash(config_parser.password_reset_value)
        connection_cursor.execute("""Update isr_registered_users SET password_hash = ? WHERE email = ?""",
                                  (hashed_password, email_id,))
        connection.commit()
        return 1
    except Exception as e:
        print("Exception occurred while resetting user's password:", e)
        return 0


if __name__ == '__main__':
    db_delete_table("isr_issues")
