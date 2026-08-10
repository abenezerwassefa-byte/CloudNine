from flask import Flask  # error says that flask is unresolved
app = Flask(__name__)


@app.route("/")
def home():
    return "CloudNine says hello!"
