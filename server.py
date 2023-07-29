from flask import Flask, send_from_directory
import os
from flask import jsonify
from dotenv import load_dotenv
from posts import request_github_projects
from utils import fetch_top_three_languages
from flask_cors import CORS
import requests
from typing import List, Dict


# To load the .env file variables
load_dotenv()

# Sets up Flask route
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_KEY")

# Sets up CORS
CORS(app)


@app.route("/get_token", methods=["GET"])
def get_token() -> List[Dict[str, any]] | str:
    """Retrieves token when fetched by front-end"""

    CLIENT_ID: str = os.getenv("CLIENT_ID")
    REDIRECT_URI: str = os.getenv("REDIRECT_URI")
    SCOPE: str = os.getenv("SCOPE")

    PARAMS: str = f"?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}"

    response = requests.get(f"https://github.com/login/oauth/authorize{PARAMS}")

    try:
        data = response.json()
        return data
    except ValueError as e:
        print(f"Decoding error: {e}")
        return jsonify({"error": "Invalid response, please try again."}), 500


@app.route("/get_user_data", methods=["GET"])
def get_data() -> List[Dict[str, any]] | None:
    """Retrieves user data"""

    response = requests.get("https://api.github.com/user")

    try:
        return response.json()
    except ValueError as e:
        print(f"Decoding error: {e}")
        return jsonify({"error": "Invalid response, please try again."}), 500


@app.route("/get_projects", methods=["GET"])
def get_projects():
    """Retrieves the projects list from Github API"""

    top_languages = fetch_top_three_languages()
    github_projects = request_github_projects(top_languages)

    return jsonify(github_projects)


# Serves static files interpreted/compiled in TS
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("client/public", path)


if __name__ == "__main__":
    app.run()
