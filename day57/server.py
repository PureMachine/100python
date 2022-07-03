from datetime import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)

def agify_user(name):
    params = {
        "name": name,
    }
    endpoint = "https://api.agify.io"
    response = requests.get(endpoint, params=params)
    j = response.json()
    return j["age"]

def gendify_user(name):
    params = {
        "name": name,
    }
    endpoint = "https://api.genderize.io"
    response = requests.get(endpoint, params=params)
    j = response.json()
    return j["gender"]

def fake_blogs():
    endpoint = "https://api.npoint.io/388f3a4a700464acebac"
    response = requests.get(endpoint)
    print(response)
    j = response.json()
    return j

@app.route('/')
def home():
    copyrt = datetime.now().year
    builder = "Puremachine"
    blogs = fake_blogs()
    return render_template("index.html", year=copyrt, builder=builder, blogs=blogs)

@app.route('/blog/<int:num>')
def blog(num: int):
    copyrt = datetime.now().year
    builder = "Puremachine"
    blogs = fake_blogs()
    return render_template("blog.html", year=copyrt, builder=builder, blogs=blogs, num=num)

@app.route('/guess/<name>')
def guess(name):
    formatted = name.title()
    age = agify_user(name)
    gender = gendify_user(name)
    copyrt = datetime.now().year
    builder = "Puremachine"
    return render_template("guess.html", formed=formatted, age=age, gender=gender, year=copyrt, builder=builder)

if __name__ == "__main__":
    app.run(debug=True)


