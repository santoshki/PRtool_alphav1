import datetime
from flask import Flask, render_template, request, redirect
from flask_login import current_user, login_user, logout_user
from models import UserModel, db, login
from database import db_insert, db_read, db_update
from parser import config_parser

app = Flask(__name__)
app.secret_key = config_parser.db_secret_key

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + config_parser.db_hostname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login.init_app(app)
login.login_view = 'login'


@app.before_request
def create_all():
    db.create_all()


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/issue_board/')
    msg = ''
    if request.method == "POST":
        try:
            if request.form["button"] == "log_in":
                print("Login button pressed.")
                email = request.form['email_id']
                user = UserModel.query.filter_by(email=email).first()
                if user is not None and user.check_password(request.form['password']):
                    print("User authenticated.")
                    login_user(user)
                    return redirect('/issue_board/')
                else:
                    msg = 'Incorrect username / password ! Please try again.'
                    print(msg)
                    return render_template('login_screen.html', msg=msg)
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
            return redirect('/existing_issues/')
    return render_template("issue_board.html")


@app.route('/existing_issues/', methods=['GET', 'POST'])
def existing_issues():
    issue_title_id_value = []
    issue_short_description_id_value = []
    issue_category_id_value = []
    issue_priority_id_value = []
    issue_assignment_group_id_value = []
    issue_created_on_id_value = []
    ticket_submitted_by_id_value = []

    no_of_issues, issue_title, issue_short_description, issue_category, issue_priority, issue_assignment_group, \
    issue_created_on, issue_submitted_by = db_read.read_data(config_parser.db_issues)
    for i in range(0, no_of_issues):
        issue_title_id_value.append("issue_title_value_" + str(i))
        issue_short_description_id_value.append("issue_short_description_value_" + str(i))
        issue_category_id_value.append("issue_category_value_" + str(i))
        issue_priority_id_value.append("issue_priority_value_" + str(i))
        issue_assignment_group_id_value.append("issue_assignment_group_value_" + str(i))
        issue_created_on_id_value.append("issue_created_on_value_" + str(i))
        ticket_submitted_by_id_value.append("ticket_submitted_by_value_" + str(i))
    return render_template("existing_issues_dashboard.html", len=no_of_issues,
                           issue_title_id_value=issue_title_id_value, issue_title=issue_title,
                           issue_short_description_id_value=issue_short_description_id_value,
                           issue_short_description=issue_short_description,
                           issue_category_id_value=issue_category_id_value, issue_category=issue_category,
                           issue_priority_id_value=issue_priority_id_value,
                           issue_priority=issue_priority,
                           issue_assignment_group_id_value=issue_assignment_group_id_value,
                           issue_assignment_group=issue_assignment_group,
                           issue_created_on_id_value=issue_created_on_id_value,
                           issue_created_on=issue_created_on, ticket_submitted_by_id_value=ticket_submitted_by_id_value,
                           ticket_submitted_by=issue_submitted_by)


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
            db_insert.register_new_issue(issue_title, issue_short_description, issue_category, issue_priority,
                                         issue_assignment_group, ct, issue_submitted_by)
        elif request.form["button"] == "browse":
            print("Browse attachments button pressed.Attachment(s) to be uploaded...")
    return render_template("new_issuev1.1.html", current_timestamp=ct)


@app.route('/sign_up/', methods=['GET', 'POST'])
def sign_up():
    ct = datetime.datetime.now()
    if current_user.is_authenticated:
        return redirect('/blogs')
    if request.method == "POST":
        if request.form["button"] == "sign_up":
            name = request.form["name"]
            username = request.form["username"]
            email_id = request.form["email_id"]
            password = request.form["password"]
            if UserModel.query.filter_by(email=email_id).first():
                return "Email already Present"
            user = UserModel(email=email_id, username=username, name=name, registration_timestamp=ct)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            print("User registration completed successfully.")
            msg = 'You have successfully registered !'
            return redirect('/login')
    return render_template("sign_up_screen.html", current_timestamp=ct)


@app.route('/forgot_password/', methods=['GET', 'POST'])
def forgot_password():
    registration_timestamp = datetime.datetime.now()
    print("Forgot password.\nNeed to reset user's password.")
    if request.method == "POST":
        if request.form["button"] == "password_reset":
            print("Resetting user's password...")
            reg_email_id_value = request.form["registered_email_id"]
            print("Registered Email id:", reg_email_id_value)
            reset_status = db_update.reset_password(email_id=reg_email_id_value)
            if reset_status:
                print("Password reset completed for the specified user. Password has been reset to ",
                      config_parser.password_reset_value)
            else:
                print("Error while resetting user's password. Unable to reset specified user's password.")
        elif request.form["button"] == "back":
            return redirect('/login')
    return render_template('forgot_password_screen.html', current_timestamp=registration_timestamp)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect('/login/')


if __name__ == '__main__':
    app.run(debug=True)
