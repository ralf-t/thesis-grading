from flask import Blueprint, render_template

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/login")
def login():
    # redir to grading if logged in
    return render_template("user/login.html")

@user.route("/read")
def read():
    #id
    #username
    #password
    #email

    users = [
        {
            "id" : "1",
            "username" : "mahabangmahabangmahabangusername",
            "password" : "123123123123123123123123123123123213",
            "email" : "ju@nd3lacruz_averyverylongemailaddresssss@email.com"
        },
        {
            "id" : "1",
            "username" : "ju@nd3lacruz",
            "password" : "123",
            "email" : "ju@nd3lacruz@email.com"
        },
        {
            "id" : "1",
            "username" : "ju@nd3lacruz",
            "password" : "123",
            "email" : "ju@nd3lacruz@email.com"
        },
        {
            "id" : "1",
            "username" : "ju@nd3lacruz",
            "password" : "123",
            "email" : "ju@nd3lacruz@email.com"
        },
        {
            "id" : "1",
            "username" : "ju@nd3lacruz",
            "password" : "123",
            "email" : "ju@nd3lacruz@email.com"
        }

    ]

    return render_template("user/read.html", users=users)