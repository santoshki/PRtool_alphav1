import sqlite3


def create_table(table_name):
    try:
        connection_db = sqlite3.connect("E:\\Entreprenuership\\PycharmProjects\\PRtool_alphav1\\entities\\isr_database.db")
        cursor_obj = connection_db.cursor()
        query = "CREATE TABLE " + str(table_name) + "(issue_title VARCHAR(255), " \
                                                    "issue_short_description VARCHAR(255),issue_category VARCHAR(255), issue_priority " \
                                                    "VARCHAR(255), issue_assignment_group VARCHAR(255), issue_submitted_by VARCHAR(255)); "
        cursor_obj.execute(query)
        print("Table created successfully!")
        cursor_obj.close()
        connection_db.commit()
    except Exception as e:
        print("Exception occurred while creating table in db", e)


if __name__ == '__main__':
    create_table("isr_new_issue")
