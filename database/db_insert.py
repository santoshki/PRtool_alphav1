import sqlite3 as sql
from usecases import encrypt


def register_user(first_name, last_name, email_id, password):
    try:
        #encoded_password = encrypt.password_encode(password)
        con = sql.connect("C:\\Users\\santosh.a.d.kulkarni\\PycharmProjects\\PRtool_alphav1\\database\\pr_database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO pr_registered_users (first_name, last_name, username, email, password) VALUES (?,?,"
                    "?,?,?)",
                    (first_name, last_name, first_name, email_id, password))
        con.commit()
        con.close()
        return 1
    except Exception as e:
        print("Exception occurred while inserting values into db", e)
        return 0
