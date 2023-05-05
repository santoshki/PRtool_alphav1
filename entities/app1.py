from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

value = []
@app.route('/input/', methods=['GET'])
def input():
    value = ["admin1", "admin2"]
    return render_template('test.html', len=2, value=value)


@app.route('/save/', methods=['POST'])
def save():
    userInput = request.form
    print(request.form.getlist('comment'))
    print(userInput)
    return render_template('home.html', userInput=userInput)


if __name__ == '__main__':
    app.run()