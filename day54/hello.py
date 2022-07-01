from flask import Flask
from functools import wraps

app = Flask(__name__)

def make_bold(func):
    @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_emph(func):
    @wraps(func)
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_undr(func):
    @wraps(func)
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

def is_logged_in(func):
    @wraps(func)
    def wrapper(**kwargs):
        return f"<u>{func(kwargs['deco'])} is logged in!</u>"
    return wrapper

@app.route("/")
@make_bold
@make_undr
@make_emph
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<username>")
def hello_user(username):
    return f"<p>Hello, World! You are {username}</p>"

@app.route("/deco/<deco>")
@is_logged_in
def hello_deco(deco):
    return f"<p>Hello, World! You are a {deco}</p>"

if __name__ == "__main__":
    app.run(debug=True)