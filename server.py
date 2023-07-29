from flask import Flask, send_from_directory, jsonify, request
import os
from dotenv import load_dotenv
from posts import request_github_projects
from utils import fetch_top_three_languages
from flask_cors import CORS
import requests
from typing import List, Dict
from urllib.parse import parse_qs

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
    CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
    code_param: str = request.args.get("code")

    PARAMS: str = f"?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={code_param}&scope=read:user,repo"

    response = requests.get(f"https://github.com/login/oauth/access_token{PARAMS}")

    try:
        content = response.content
        # Decode byte string
        access_token_string = content.decode("utf-8")

        # Use urllib to grab access token param
        query_params = parse_qs(access_token_string)
        data = query_params["access_token"][0]
        print(f"Data returned to front end: {data}")
        return data
    except ValueError as e:
        print(f"Decoding error: {e}")
        return jsonify({"error": "Invalid response, please try again."}), 500


@app.route("/get_user_data", methods=["GET"])
def get_data() -> List[Dict[str, any]] | None:
    """Retrieves user data"""

    access_token = request.headers.get("Authorization")
    print(access_token)

    if not access_token:
        return jsonify({"error": "No authorization header."}), 401

    auth = "Bearer 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"
    headers = {"Authorization": auth}

    response = requests.get("https://api.github.com/user", headers=headers)
    print(f"Response: {response.text}\n")
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
