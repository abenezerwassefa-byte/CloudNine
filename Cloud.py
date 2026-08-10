from flask import Flask  # error says that flask is unresolved
app = Flask(__name__)


@app.route("/about")
def home():
    return "CloudNine says hello!"
