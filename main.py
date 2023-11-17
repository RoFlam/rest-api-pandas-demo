from flask import Flask
from flask.json import jsonify

app = Flask(__name__)  # Flask("main.py") --> INSTANCIRANJE FLASK OBJEKTA

# @app.route("/") # --> ISHODISNA RUTA A LA GOOGLE.CO; NASA JE http://127.0.0.1--> LOCALHOST
# def hello_world():
#     return "<P>Hello World</p>"



dict_primjer = {
    "ime": "Marko",
    "prezime": "Markic",
    "email": "marko@mail.com"
}

@app.route("/")
def home():
     return "<h1><a href='/about'>Home page</a></h1>"

@app.route("/about")
def about():
    return "<p>About page</p>"

@app.route("/user/<username>")
def user(username):
    return f"<h3>User page for: {username}</h3>" # vraca HTML

@app.route("/json")
def json():
    return jsonify(dict_primjer)

@app.route("/json/<key>")
def json_value(key):
    return dict_primjer.get(key, "Unknown key") # --> key pisi malim slovom (umjsto "Ime" --> "ime")

