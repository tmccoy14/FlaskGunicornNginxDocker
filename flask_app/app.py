from flask import Flask

# Basic Flask app

server = Flask(__name__)


@server.route("/")
def hello_world():
    return "hello world!"
