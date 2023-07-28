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

github = oauth.register(
    name="github",
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    access_token_url="https://github.com/login/oauth/access_token",
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",
    authorize_params=None,
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "user:public_data"},
)

# Stores users data
DATA = []


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


@app.route("/login")
def github_login():
    redirect_url = url_for("authorize", _external=True)
    return github.authorize_redirect(redirect_url)


@app.route("/callback")
def authorize():
    USER_ACCESS_TOKEN = github.authorize_access_token()
    response = github.get("user", token=USER_ACCESS_TOKEN)

    USER_PROFILE = response.json()

    # Create instance of User object and store in list
    DATA.append(User(USER_ACCESS_TOKEN, USER_PROFILE))

    # Create redirect URL
    redirect_url = url_for("base", token=USER_ACCESS_TOKEN)

    return redirect(redirect_url)


if __name__ == "__main__":
    app.run()
