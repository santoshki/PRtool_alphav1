import sqlite3 as sql
from parser import config_parser


def read_data(table_name):
    try:
        con = sql.connect(config_parser.db_hostname)
        cur = con.cursor()
        read_query = "SELECT * FROM " + table_name
        cur.execute(read_query)
        data = cur.fetchall()
        if table_name == config_parser.db_issues:
            issue_title = []
            issue_short_description = []
            issue_category = []
            issue_priority = []
            issue_assignment_group = []
            issue_created_on = []
            issue_submitted_by = []
            for details in data:
                issue_title.append(details[0])
                issue_short_description.append(details[1])
                issue_category.append(details[2])
                issue_priority.append(details[3])
                issue_assignment_group.append(details[4])
                issue_created_on.append(details[5])
                issue_submitted_by.append(details[6])
                con.close()
            no_of_issues = len(issue_title)
            print("Total number of existing issues:", no_of_issues)
            return no_of_issues, issue_title, issue_short_description, issue_category, issue_priority, issue_assignment_group, \
                       issue_created_on, issue_submitted_by
        elif table_name == config_parser.db_users:
            print(data)
            return data
        else:
            print("Invalid table name")
            return None
    except Exception as e:
        print("Exception occurred while trying to read existing issues from the db", e)


if __name__ == '__main__':
    read_data("isr_issues")
