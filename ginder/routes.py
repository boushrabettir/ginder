from flask import Flask, redirect

app = Flask(__name__)

# Hold client id
CLIENT_ID = ""


@app.route("/")
def login_through_github():
    redirect_url = f"https://github.com/login/oauth/authorize?client_id={CLIENT_ID}"
    return redirect(redirect_url, code=302)


if __name__ == "__main___":
    app.run()
