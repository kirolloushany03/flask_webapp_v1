from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '8b11d0915342f71c48a8e426d0450ba0' #secret key for the application security thing
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #this the function of our route
login_manager.login_message_category = 'info'

from flaskblog import routes

# with app.app_context():
#     db.create_all()
