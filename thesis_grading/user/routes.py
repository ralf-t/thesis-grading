from flask import Blueprint, render_template

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/login")
def login():
    # redir to grading if logged in
    return render_template("user/login.html")