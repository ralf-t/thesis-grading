from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    # redir to login if anon
    # redir to thesis read if logged in
    return "hello"