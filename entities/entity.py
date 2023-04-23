from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/new_issue/', methods=['GET', 'POST'])
def new_issue():
    if request.method == "POST":
        form_data = request.form
        issue_title = form_data["issue_title"]
        if request.form["submit_button"] == "submit":
            print(issue_title)
    return render_template("new_issuev1.1.html")


@app.route('/sign_up/', methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up_screen.html")


if __name__ == '__main__':
    app.run(debug=True)
