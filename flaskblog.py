#!/usr/bin/python3
from flask import Flask, render_template, url_for

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
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='Aboutpage')

if __name__ == "__main__":
    app.run(debug=True)





