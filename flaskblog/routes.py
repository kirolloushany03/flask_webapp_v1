#!/usr/bin/python3
from flask import render_template, url_for, flash, redirect
from flaskblog import app, bcrypt, db
from flaskblog.forms import RegistrationForm, Loginform
from flaskblog.models import User, Post




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
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('your account created and you are able to log in', 'success')
        return redirect(url_for('login'))
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
