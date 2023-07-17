from flask import Flask, redirect

app = Flask(__name__)

# Hold client id
CLIENT_ID = ""


@app.route("/login")
def login_through_github():
    redirect_url = f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}"
    return redirect(redirect_url, code=302)


if __name__ == "__main___":
    app.run()


"""
Another idea - Boushra
"""
from flask_github import GitHub

app.config["GITHUB_CLIENT_ID"] = ""
app.config["GITHUB_CLIENT_SECRET"] = ""

app.config["GITHUB_BASE_URL"] = ""
app.config["GITHUB_AUTH_URL"] = ""

gh = GitHub(app)


@app.route("/login")
def login_through_github():
    return gh.authorize()


@app.route("/callback")
@gh.authorized_handler
def authorization(oauth_token: str):
    if not oauth_token:
        print("Failed.")
        return redirect("/")

    user = User.query.filter_by(github_access_token=oauth_token).first()
    if not user:
        pass
        # Create new user instance (Create User dataclass?)
        # Add our user to our session

    user.github_access_token = oauth_token
    # Hold token somewhere

    # Return back to our URL
