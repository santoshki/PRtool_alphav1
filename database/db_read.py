import sqlite3 as sql

con = sql.connect("pr_database.db")
cur = con.cursor()
cur.execute("SELECT * FROM pr_registered_users")
users = cur.fetchall()
print(users)
con.close()