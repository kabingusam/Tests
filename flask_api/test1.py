from markupsafe import escape
from flask import Flask
app = Flask(__name__)


@app.route('/user/username')
def show_user_profile(username):
    # show the user profile
    return'User %s' %escape(username)