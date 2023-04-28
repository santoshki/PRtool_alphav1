import datetime

from werkzeug.security import generate_password_hash

from usecases import config_parser, encrypt
from database import db_insert
from flask import Flask, render_template, request, redirect
from flask_login import login_required, current_user, login_user, logout_user, LoginManager
from models import UserModel, db, login


app = Flask(__name__)
app.secret_key = 'xyz'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\santosh.a.d.kulkarni\\PycharmProjects\\PRtool_alphav1\\database\\pr_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login.init_app(app)
login.login_view = 'login'
login_manager = LoginManager()
login_manager.init_app(app)


"""@app.before_first_request
def create_all():
    db.create_all()"""


@login_manager.user_loader
def load_user(user):
    return user.get(user)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == "POST":
        try:
            if request.method == "POST":
                if request.form["button"] == "log_in":
                    print("Login button pressed.")
                    email_id_value = request.form.get("email_id")
                    password_value = request.form.get("password")
                    encoded_password = encrypt.password_encode(password_value)
                    user = UserModel.query.filter_by(email=email_id_value).first()
                    if user is not None and user.check_password(password_value):
                        login_user(user)
                        print("User authenticated.")
                        return redirect('/issue_board/')
                    else:
                        msg = 'Incorrect username / password ! Please try again.'
                        print(msg)
                        return render_template('login.html', msg=msg)
        except Exception as e:
            print("Exception occurred:", e)
    return render_template('login_screen.html', msg=msg)


@app.route('/issue_board/', methods=['GET', 'POST'])
def issue_board():
    if request.method == "POST":
        if request.form["button"] == "new_issue":
            print("Creating a new issue as per user's request, redirecting to new issue creation page....")
            return redirect('/new_issue/')
        elif request.form["button"] == "existing_issues":
            print("Opening existing issues list")
    return render_template("issue_board.html")


@app.route('/new_issue/', methods=['GET', 'POST'])
def new_issue():
    ct = ""
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
        elif request.form["button"] == "browse":
            print("Browse attachments button pressed.Attachment(s) to be uploaded...")
    return render_template("new_issuev1.1.html", current_timestamp=ct)


@app.route('/sign_up/', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        if request.form["button"] == "sign_up":
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            email_id = request.form["email_id"]
            password = request.form["password"]
            username = first_name[:4] + last_name[:2]
            reg_user = db_insert.register_user(first_name, last_name, email_id, password=)
            if reg_user:
                print("Data inserted successfully into db. User registration completed successfully.")
            else:
                print("Error while inserting data into db. User registration pending.")
            msg = 'You have successfully registered !'
    return render_template("sign_up_screen.html")


@app.route('/forgot_password/', methods=['GET', 'POST'])
def forgot_password():
    registration_timestamp = datetime.datetime.now()
    print("Forgot password.\nNeed to reset user's password.")
    if request.method == "POST":
        if request.form["button"] == "password_reset":
            print("Resetting user's password...")
            reg_email_id_value = request.form["registered_email_id"]
            print("Registered Email id:", reg_email_id_value)
            #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            #cursor.execute('SELECT * FROM user_credentials WHERE email_id = % s', (reg_email_id_value,))
            #account = cursor.fetchone()
            #print("User account details:", account)
            #cursor.execute('Update user_credentials SET password = %s WHERE email_id = % s',
                           #('tested123', reg_email_id_value,))
            #print("Password has been reset")
            #mysql.connection.commit()
            #cursor.execute('SELECT * FROM user_credentials WHERE email_id = % s', (reg_email_id_value,))
            #account = cursor.fetchone()
            #print("Updated record:", account)
        elif request.form["button"] == "back":
            return render_template('login.html')
    return render_template('forgot_password_screen.html', current_timestamp=registration_timestamp)


if __name__ == '__main__':
    app.run(debug=True)
