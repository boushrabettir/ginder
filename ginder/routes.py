from flask import Flask, redirect, url_for, render_template
import os
from authlib.integrations.flask_client import OAuth
import dotenv

app = Flask(__name__)
oauth = OAuth(app)
app.secret_key = os.getenv('SECRET_KEY')

github = oauth.register(
    name = 'github',
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    access_token_url='https://github.com/login/oauth/access_token', # This is the url that the access token is retrieved from
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize', # This is the url that the user is redirected to to authorize the app
    authorize_params=None,
    api_base_url='https://api.github.com/', # This is the base url for the github api
    client_kwargs={'scope': 'user:public_data'} # This is the scope of the data that the app will be able to access
)

@app.route('/')
def testing():
    return 'FRONT PAGE' # this is for testing purposes for now to make sure people are redirected here after logging in

@app.route('/login')
def github_login():
    redirect_url = url_for("authorize", _external=True) # This is the url that the user will be redirected to after they authorize the app
    return github.authorize_redirect(redirect_url) # This redirects the user to the authorization page

@app.route('/callback')
def authorize():
    token = github.authorize_access_token() # This gets the access token to access the user's information to be able to use it in the app
    response = github.get('user', token=token) # This gets the user's information.
    user_profile = response.json() # This converts the user's information to json format
    print(user_profile, token) # This prints the user's information and the access token
    return render_template('github.html', user=user_profile) # This renders the github.html template and passes the user's information to it

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# followed this tutorial utilizing authlib to create authentication with flask and github: https://dev.to/nelsoncode/authentication-with-flask-and-github-authlib-19ej
# this is the documentation for the library: https://docs.authlib.org/en/latest/client/flask.html#routes-for-authorization
# https://pygithub.readthedocs.io/en/latest/introduction.html