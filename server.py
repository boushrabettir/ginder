from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
from posts import request_github_projects
from reccomendation import get_filtered_reccomendation
from utils import fetch_user_languages
from flask_cors import CORS
import requests
from posts import OpenSource
from typing import List, Dict
from urllib.parse import parse_qs
import json

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

    response_params: str = f"?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={code_param}&scope=read:user,repo"

    response = requests.get(
        f"https://github.com/login/oauth/access_token{response_params}"
    )

    try:
        content = response.content
        # Decode byte string
        access_token_string = content.decode("utf-8")

        # Use urllib to grab access token param
        query_params = parse_qs(access_token_string)
        data = query_params["access_token"][0]

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

    auth_headers = {"Authorization": headers}
    response = requests.get("https://api.github.com/user", headers=auth_headers)

    try:
        return response.json()
    except ValueError as e:
        print(f"Decoding error: {e}")
        return jsonify({"error": "Invalid response, please try again."}), 500


@app.route("/get_projects", methods=["POST", "GET"])
def get_projects():
    """Retrieves the projects list from Github API"""

    # Retrieves token from front end post request
    if request.method == "POST":
        post_rq_data = request.get_json()
        token = post_rq_data.get("token")

    top_languages = fetch_user_languages(token)

    github_projects: List[OpenSource] = request_github_projects(top_languages, token)

    seralized_data = [
        {
            "id": data.id,
            "name": data.name,
            "desc": data.description,
            "link": data.link,
            "username": data.username,
            "languages": data.languages,
            "stars": data.stars,
            "forks": data.forks,
            "contributers": data.contributers,
            "followers": data.followers,
        }
        for data in github_projects
    ]

    response_object = {
        "serialized_data": seralized_data,
        "top_languages": top_languages,
    }

    return jsonify(response_object)


@app.route("/get_next_group", methods=["POST", "GET"])
def get_next_group():
    """Retrieves the next group of projects to be sent to the frontend"""

    if request.method == "POST":
        post_rq_data = request.get_json()
        right_swipes_data = post_rq_data.get("data")
        token = post_rq_data.get("token")

    filtered_reccomendation: List[OpenSource] = get_filtered_reccomendation(
        right_swipes_data, token
    )

    serialized_data = [
        {
            "id": data.id,
            "name": data.name,
            "desc": data.description,
            "link": data.link,
            "username": data.username,
            "languages": data.languages,
            "stars": data.stars,
            "forks": data.forks,
            "contributers": data.contributers,
            "followers": data.followers,
        }
        for data in filtered_reccomendation
    ]

    return jsonify(serialized_data)


@app.route("/add_to_stars", methods=["POST", "GET"])
def add_to_stars() -> str | None:
    """Add project to stars from local storage"""

    if request.method == "POST":
        post_rq_data = request.get_json()
        project_data: List[object] = json.loads(post_rq_data.get("data"))
        token = post_rq_data.get("token")

    if not token:
        return jsonify({"error": "No token given"}), 401

    headers = {"Authorization": f"Bearer {token}"}

    for project in project_data:
        owner = project["username"]
        repo_name = project["name"]

        # https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28
        request_url = f"https://api.github.com/user/starred/{owner}/{repo_name}"
        try:
            response = requests.put(request_url, headers=headers)

            if response.status_code == 204:
                return "Project added successfully"

        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Error adding repo to Github stars list: {e}"})


if __name__ == "__main__":
    app.run()
