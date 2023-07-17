from flask import Flask, current_app

app = Flask(__name__)


@app.route("/")
def temp():
    return current_app.send_static_file("test.html")
