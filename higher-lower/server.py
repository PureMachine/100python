from flask import Flask
from functools import wraps
import random

app = Flask(__name__)


def make_bold(func):
    @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def make_h1(func):
    @wraps(func)
    def wrapper():
        return f"<h1>{func()}</h1>"
    return wrapper

def make_random_color(func):
    colors = ["red", "blue",  "green"]
    chosen_color = random.choice(colors)
    @wraps(func)
    def wrapper(**kwargs):
        return f"<h1 style='color:{chosen_color};'>{func(kwargs['random_number'])}</h1>"
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
        return f"<u>{func(kwargs['random_number'])} is logged in!</u>"
    return wrapper

def generate_number():
    return random.randrange(1, 9)

@app.route("/")
@make_h1
def hello_world():
    content = "Guess a number between 0 and 9<br>" \
              "<img src='https://media.giphy.com/media/D7z8JfNANqahW/giphy.gif'>"
    return content

@app.route("/<int:random_number>")
@make_random_color
def random_path(random_number):
    global target
    if random_number > target:
        return "Too high"
    elif random_number < target:
        return "Too low"
    else:
        return "Just right"

@app.before_request
def generate_number():
    global target
    target = random.randrange(1, 9)


if __name__ == "__main__":
    target: int
    app.run(debug=True)
