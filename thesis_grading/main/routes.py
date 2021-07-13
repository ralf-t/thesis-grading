from flask import Blueprint, redirect, url_for
from flask_login import current_user

main = Blueprint("main", __name__)

@main.route("/")
def home():
    if current_user.is_authenticated:
        # redir to grading feed
        "hello"
    
    return redirect(url_for("user.login"))