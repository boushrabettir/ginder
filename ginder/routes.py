from flask import Flask, redirect, url_for, send_from_directory, render_template
import os
from flask import jsonify
from authlib.integrations.flask_client import OAuth
import dotenv
from posts import request_github_projects
from utils import fetch_top_three_languages
from flask_cors import CORS


app = Flask(__name__)
oauth = OAuth(app)
app.secret_key = "27edbe3dbu8dvuqsnu217ybsj1ns284dba82128eghsbs273rgzx3e9xz"

CORS(app)

github = oauth.register(
    name="github",
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    access_token_url="https://github.com/login/oauth/access_token",  # This is the url that the access token is retrieved from
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",  # This is the url that the user is redirected to to authorize the app
    authorize_params=None,
    api_base_url="https://api.github.com/",  # This is the base url for the github api
    client_kwargs={
        "scope": "user:public_data"
    },  # This is the scope of the data that the app will be able to access
)


@app.route("/")
def login_page():
    pass


# Base route
@app.route("/home")
def base():
    return render_template("index.html")


# Serves static files interpreted/compiled in TS
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("client/public", path)


@app.route("/get_projects", methods=["GET"])
def get_projects():
    top_languages = fetch_top_three_languages()
    github_projects = request_github_projects(top_languages)
    return jsonify(github_projects)


@app.route("/login")
def github_login():
    redirect_url = url_for(
        "authorize", _external=True
    )  # This is the url that the user will be redirected to after they authorize the app
    return github.authorize_redirect(
        redirect_url
    )  # This redirects the user to the authorization page


@app.route("/callback")
def authorize():
    token = github.authorize_access_token()  # This gets the access token
    response = github.get("user", token=token)  # This gets the user's information
    user_profile = (
        response.json()
    )  # This converts the user's information to json format
    print(
        user_profile, token
    )  # This prints the user's information and the access token
    return redirect("/")  # This redirects the user to the front page of the website


if __name__ == "__main__":
    app.run()

# followed this tutorial utilizing authlib to create authentication with flask and github: https://dev.to/nelsoncode/authentication-with-flask-and-github-authlib-19ej
# this is the documentation for the library: https://docs.authlib.org/en/latest/client/flask.html#routes-for-authorization
# https://pygithub.readthedocs.io/en/latest/introduction.html
