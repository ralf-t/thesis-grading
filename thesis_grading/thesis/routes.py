from flask import Blueprint, render_template, request, redirect, url_for
from pprint import pprint

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
            "title" : "Lorem ipsum dolor set go run forrest run, run to make this title longer",
            "chairman" : "Dela Cruz, Juan",
            "group_number" : 1,
            "proponents" : ['20190151324','20181534568','20153156821','20131568824'],
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
       {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
        },
       {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
        },
       {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
        },
       {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
        },
       {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
        },
       {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
        },
       {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
        },
       {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
        },
       {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Doe, John",
            "group_number" : 3,
            "proponents" : ['XXXXXXX','XXXXXXX','XXXXXXX'],
            "adviser" : "Hwang, Yeji",
            "program_name" : "BSEMC-GD"
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

@thesis.route("/create", methods=["GET","POST"])
def create():

    return render_template("thesis/create.html")