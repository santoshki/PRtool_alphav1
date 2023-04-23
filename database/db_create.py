import sqlite3

connection_db = sqlite3.connect("pr_database.db")
cursor_obj = connection_db.cursor()
create_table = """CREATE TABLE PR_ISSUES(Issue_title VARCHAR(255));"""

cursor_obj.execute(create_table)
print("Table created successfully!")
cursor_obj.close()
