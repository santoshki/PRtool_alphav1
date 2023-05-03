import sqlite3 as sql
from usecases import encrypt
from parser import config_parser


def register_new_issue(issue_title, issue_short_description, issue_category, issue_priority, issue_assignment_group,
                       issue_submitted_by):
    connection = sql.connect(config_parser.db_hostname)
    connection_cursor = connection.cursor()
    connection_cursor.execute(
        "INSERT INTO isr_new_issue (issue_title, issue_short_description, issue_category, issue_priority, issue_assignment_group, issue_submitted_by) VALUES (?,?,?,?,?,?)",
        (issue_title, issue_short_description, issue_category, issue_priority, issue_assignment_group,
         issue_submitted_by))
    connection.commit()
    connection.close()
    print("New issue details registered successfully.")


def register_user(first_name, last_name, email_id, password):
    try:
        # encoded_password = encrypt.password_encode(password)
        con = sql.connect(config_parser.db_hostname)
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
