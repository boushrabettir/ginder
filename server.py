from flask import Flask, send_from_directory, jsonify, request
import os
from dotenv import load_dotenv
from posts import request_github_projects
from reccomendation import get_filtered_reccomendation
from posts import OpenSource

# from utils import fetch_top_three_languages
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

    headers = request.headers.get("Authorization")

    if not headers:
        return jsonify({"error": "No authorization header."}), 401

    temp = {"Authorization": headers}
    response = requests.get("https://api.github.com/user", headers=temp)

    try:
        return response.json()
    except ValueError as e:
        print(f"Decoding error: {e}")
        return jsonify({"error": "Invalid response, please try again."}), 500


@app.route("/get_projects", methods=["GET"])
def get_projects():
    """Retrieves the projects list from Github API"""

    top_languages = ["python", "rust", "c++"]
    github_projects = request_github_projects(top_languages)

    seralized_data = [
        {
            "id": data.id,
            "name": data.name,
            "desc": data.description,
            "link": data.link,
            "owner": data.owner,
            "languages": data.languages,
            "stars": data.stars,
        }
        for data in github_projects
    ]

    response_object = {
        "serialized_data": seralized_data,
        "top_languages": top_languages,
    }

    return jsonify(response_object)


@app.route("/get_next_group", methods=["GET"])
def get_next_group():
    """Retrieves the next group of projects to be sent to the frontend"""

    filtered_reccomendation = get_filtered_reccomendation()

    serialized_data = [
        {
            "id": data.id,
            "name": data.name,
            "desc": data.description,
            "link": data.link,
            "owner": data.owner,
            "languages": data.languages,
            "stars": data.stars,
        }
        for data in filtered_reccomendation
    ]

    return jsonify(serialized_data)


# Serves static files interpreted/compiled in TS
@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory("client/public", path)


if __name__ == "__main__":
    app.run()
