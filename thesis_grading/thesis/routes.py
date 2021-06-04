from flask import Blueprint, render_template

thesis = Blueprint("thesis", __name__, url_prefix="/thesis")

@thesis.route("/read")
def read():
    # redir to grading if logged in

    # title 
    # chairman 
    # group number
    # proponents (student numbers)
    # adviser 
    # program

    theses = [
        {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Dela Cruz, Juan",
            "group_number" : 1,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Shin, Ryujin",
            "program_name" : "BSCS"
        },
        {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Ng, Andrew",
            "group_number" : 2,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Kang, Seulgi",
            "program_name" : "BSIT"
        },
        {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
        },
    ]

    return render_template("thesis/read.html", theses=theses)