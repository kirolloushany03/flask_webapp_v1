#!/usr/bin/python3

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.column(db.integer, primary_key=True)
    content = db.column(db.string(200), nullable=False)
    date_created = db.column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
    
@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/about")
def about():
    return "hellow"


if __name__ == "__main__":
    app.run(debug=True)