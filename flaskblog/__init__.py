from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8b11d0915342f71c48a8e426d0450ba0' #secret key for the application security thing
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)



from flaskblog import routes

# with app.app_context():
#     db.create_all()
