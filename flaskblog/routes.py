#!/usr/bin/python3
import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, bcrypt, db
from flaskblog.forms import RegistrationForm, UpdateAccountForm ,Loginform
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Loginform()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('login unsccessful. please chech email and password', 'danger')
    return render_template("login.html", title='login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your Account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                            image_file=image_file, form=form)

# what we did here that why we put ther return redirect int this line return redirect(url_for('account'))
# this because sth called post get redirect pattern
# post from the browser
# redirect from the server to another url
# get from the browser


# after elif he talked that if i just clicked the button and said change the username and password
# then he will change and redirect
#but if i didnt make GET request as usual
# form = UpdateAccountForm()
#     if form.validate_on_submit():
#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.commit()
#         flash('your account has been updated', 'success')
#         return redirect(url_for('account'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.email.data = current_user.email


# to login
# email : "kiro3@gmail.com" username : "kirooo"  pass : "kiro12"
# email : "kiro322@gmail.com" username : "kiro" pass : "kiro"
# 
# 