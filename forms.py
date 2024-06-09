from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#this the registration form
class RegistrationForm(FlaskForm):
    username = StringField('username',
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password= PasswordField('password',
                            validators=[DataRequired()])
    confirm_password= PasswordField('password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')

# this the loging form 
class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password= PasswordField('password',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')