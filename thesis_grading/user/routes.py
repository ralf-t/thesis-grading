from flask import Blueprint, render_template

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/login")
def login():
    # redir to grading if logged in
    return render_template("user/login.html")

@user.route("/password/reset")
def reset():
    
    return render_template("user/password_reset.html")

@user.route("/read")
def read():
    
    return render_template("user/read.html")