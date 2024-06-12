#!/usr/bin/python3
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, Loginform

app = Flask(__name__)

app.config['SECRET_KEY'] = '8b11d0915342f71c48a8e426d0450ba0' #secret key for the application security thing
posts =[
    {
        "author":"kirollous hany",
        "title": "blog post 1",
        "content":"first post content",
        "date" : "april 20, 2024"
    },
    {
        "author":"ali ba7a",
        "title": "blog post 2",
        "content":"secound post content",
        "date" : "april 21, 2024"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='Aboutpage')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        if form.email.data == "1234@gmail.com" and form.password.data == '123456':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsccessful. please chech username and password', 'danger')
    return render_template("login.html", title='login', form=form)


if __name__ == "__main__":
    app.run(debug=True)





