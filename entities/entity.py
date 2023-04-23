from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import datetime
from usecases import config_parser, encrypt
from database import db_read

app = Flask(__name__)
app.secret_key = config_parser.secret_key
app.config['MYSQL_HOST'] = config_parser.db_hostname
app.config['MYSQL_USER'] = config_parser.db_username
app.config['MYSQL_PASSWORD'] = config_parser.db_password
app.config['MYSQL_DB'] = config_parser.db_name
mysql = MySQL(app)

app = Flask(__name__)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        msg = ''
        try:
            if request.method == "POST":
                if request.form["button"] == "log_in":
                    print("Login button pressed.")
                    email_id_value = request.form.get("email_id")
                    password_value = request.form.get("password")
                    encoded_password = encrypt.password_encode(password_value)
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute('SELECT * FROM user_credentials WHERE email_id = % s AND password = % s',
                                   (email_id_value, encoded_password,))
                    account = cursor.fetchone()
                    if account:
                        session['loggedin'] = True
                        session['id'] = account['id']
                        session['email_id'] = account['email_id']
                        msg = 'Logged in successfully !'
                        print("Login Successful.")
                        return redirect('/dashboard/')
                    else:
                        msg = 'Incorrect username / password ! Please try again.'
                        print(msg)
                        return render_template('login.html', msg=msg)

        except Exception as e:
            print("Exception occurred:", e)
        return render_template('login_screen.html', msg=msg)


@app.route('/new_issue/', methods=['GET', 'POST'])
def new_issue():
    if request.method == "POST":
        ct = datetime.datetime.now()
        form_data = request.form
        if request.form["button"] == "submit":
            print("Submit button pressed, capturing user inputs....")
            issue_title = form_data["issue_title"]
            issue_short_description = form_data["issue_short_description"]
            issue_category = form_data.get("issue_category")
            issue_priority = form_data.get("issue_priority")
            issue_assignment_group = form_data.get("assignment_group")
            issue_submitted_by = form_data.get("ticket_submitted_by")
            print(issue_title)
            print(issue_short_description)
            print(issue_category)
            print(issue_priority)
            print(issue_assignment_group)
            print(issue_submitted_by)
        elif request.form["button"] == "browse":
            print("Browse attachments button pressed.Attachment(s) to be uploaded...")
    return render_template("new_issuev1.1.html", current_timestamp=ct)


@app.route('/sign_up/', methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up_screen.html")


if __name__ == '__main__':
    app.run(debug=True)
