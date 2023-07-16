# TODO - Github Properties
import requests

# TODO (boushra)
# Sama, please research how everything will flow together, please ensure all code works.
# For myself, help her with this OAuth Process + create static HTML page + set up simple route

GITHUB_ENDPOINT = "https://api.github.com"


def request_identity(
    client_id: str,
    redirect_uri: str,
    login: str,
    scope: str,
    state: str,
    allow_signup: str,
):
    """Verify the user and get the authorization code"""

    data = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "login": login,  # The specific account used for signing in and authorizing the app
        "scope": scope,  # The limit to an application's access to a user's account
        "state": state,  # An unguessable random string to protect against cross-site request forgery attacks.
        "allow_signup": allow_signup,  # Whether or not unauthenticated users will be offered an option to sign up for GitHub during the OAuth flow.
    }
    authorize_app = requests.post(
        f"{GITHUB_ENDPOINT}/oauth/authorize", data=data
    )  # The request to authorize the app, data=data is the data that is sent to the api
    return authorize_app.json()  # Returns the authorization code


def redirect_to_github(
    client_id: str, client_secret: str, code: str, redirect_uri: str
):
    """Gets the access token"""

    data = {
        "client_id": client_id,  # Identifies the app, like a username
        "client_secret": client_secret,  # This is the password for the app
        "code": code,  # The code that is returned from the authorization
        "redirect_uri": redirect_uri,  # The url that people will be redirected to after they authorize the app
    }
    access_token_request = requests.post(
        f"{GITHUB_ENDPOINT}/oauth/access_token", data=data
    )  # The request to get the access token
    return (
        access_token_request.json()
    )  # Returns the access token which is used to make requests to the api


def verify_user(
    client_id: str,
    scope: str,
    device_code: str,
    user_code: str,
    verification_uri: str,
    expires_in: int,
    interval: int,
):
    """Returns a device verification code that the app must use to receive an access token and check the status of user authentication."""
    data = {
        "client_id": client_id,
        "scope": scope,
        "device_code": device_code,  # The device verification code that the app must use to receive an access token and check the status of user authentication.
        "user_code": user_code,  # The code that must be entered for verification
        "verification_uri": verification_uri,  # The url that people will be redirected to after they authorize the app
        "expires_in": expires_in,  # the time before the code expires
        "interval": interval,  # The time that must pass before a user can make a new request
    }
    verification_code = requests.post(
        f"{GITHUB_ENDPOINT}/login/device/code", data=data
    )  # The request is to get the verification code
    return verification_code.json()  # Returns the verification code in json format


def check_authorization(client_id: str, device_code: str, grant_type: str):
    """Check if the user has authorized the app"""

    data = {
        "client_id": client_id,
        "device_code": device_code,
        "grant_type": grant_type,  # The type of grant that is being requested which must be urn:ietf:params:oauth:grant-type:device_code
    }
    authorization = requests.post(
        f"{GITHUB_ENDPOINT}/login/oauth/access_token", data=data
    )  # The request to check if the user has authorized the app
    return authorization.json()  # Returns the authorization in json format
