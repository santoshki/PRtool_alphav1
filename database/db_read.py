import sqlite3 as sql

con = sql.connect("E:\\Entreprenuership\\PycharmProjects\\PRtool_alphav1\\entities\\isr_database.db")
cur = con.cursor()
cur.execute("SELECT * FROM isr_new_issue")
users = cur.fetchall()
print(users)
con.close()