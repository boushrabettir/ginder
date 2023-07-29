from flask import Flask, redirect, url_for, send_from_directory, render_template
import os
from flask import jsonify
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from posts import request_github_projects
from utils import fetch_top_three_languages
from flask_cors import CORS
from user import User

# To load the .env file variables
load_dotenv()

# Sets up Flask route
app = Flask(__name__)
# Create OAuth app
oauth = OAuth(app)
app.secret_key = os.getenv("FLASK_KEY")

# Sets up CORS
CORS(app)


# Stores users data
DATA = []

# TODO - Update this dependent on server.js


# Login route
@app.route("/")
def login_page():
    return render_template("login.html")


# Base homepage route
@app.route("/home/<token>")
def base():
    return render_template("index.html")


# Serves static files interpreted/compiled in TS
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("client/public", path)


# Retrieves the projects list from Github API
@app.route("/get_projects", methods=["GET"])
def get_projects():
    top_languages = fetch_top_three_languages()
    github_projects = request_github_projects(top_languages)
    return jsonify(github_projects)


if __name__ == "__main__":
    app.run()
