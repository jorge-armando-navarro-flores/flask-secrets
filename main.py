from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

app = Flask(__name__)


class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')


app.secret_key = "some secret string"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

