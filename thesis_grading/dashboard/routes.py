from flask import Blueprint, render_template
from json import dumps

dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard.route("/")
def read():

    thesis = {
            "title" : "Lorem ipsum dolor set go run forrest run",
            "chairman" : "Dela Cruz, Juan",
            "group_number" : 1,
            "proponents" : ["Policarpio, Jon Theo",
                            "Torres, Karryl Dale",
                            "Sibulo, Tovi Jet",
                            "Tuazon, Kriss",
                            "Seneca, John Pocholo"],
            "adviser" : "Shin, Ryujin",
            "program_name" : "BSCS"
        }

    course = {
        "criterias": ["Character Development",
                        "Environment Development",
                        "Animation",
                        "Sound Elements",
                        "Screenplay",
                        "Manuscript"],
        "assessments": ["Passed",
                        "Conditional Pass",
                        "Redefense",
                        "Failed"]
        }

    return render_template(
        "dashboard/read.html", 
        thesis=thesis, 
        course=course)
    # return render_template("dashboard/read.html")
