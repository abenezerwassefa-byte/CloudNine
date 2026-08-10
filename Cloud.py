# error says that flask is unresolved. render_template is a function and request is an object
from flask import Flask, render_template, request
app = Flask(__name__)


# this route is allowed to receive both GET and POST requests.
@app.route("/", methods=["GET", "POST"])
def home():
    city = "London"
    if request.method == "POST":
        city = request.form["city"]
        print(city)

    # message is an argument that
    return render_template("cloud.html", message="Welcome to CloudNine!!", city=city)


@app.route("/about")
def about():
    return "CloudNine is a weather app built with Flaskkkk"
