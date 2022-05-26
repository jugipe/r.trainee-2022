"""
Reaktor Fall 2022 Software developer trainee
Preliminary Assignment

This Python program is a small poetry.lock file parser and visualizer for depencies
used in a project. It contains a backend written in python using flask microframework
and has a basic html front using jinja2 to render the webpages.
"""
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from tomlparser import TomlParser
import os

app = Flask(__name__)

@app.route("/")
def upload_file():
    """Starting page for the user"""
    return render_template("upload.html")

@app.route("/index", methods=["GET", "POST"])
def after_file_upload():
    """Function which contains the program logic after file upload. Uses a parser
    to parse the given poetry.lock file to visualizable form. Redirects the user
    back to mainpage, if the user uploads something else than a poetry.lock file.
    """

    if request.method == "POST":

        file = request.files["file"]
        file.save(secure_filename(file.filename))
        
        # Parse the uploaded file 
        after_file_upload.parsed_TOML = TomlParser(
            secure_filename(file.filename))

        # Remove the file after parsing to keep disk usage at minimum
        os.remove(secure_filename(file.filename))

        # Make sure that the parser returns data to visualize and kindly ask the user
        # to upload a .lock file otherwise.
        if after_file_upload.parsed_TOML.get_data() == None or len(after_file_upload.
                                                        parsed_TOML.get_data()) == 0:

            return render_template("upload.html", error="Please upload a .lock file")

        return render_template("index.html", 
            value=after_file_upload.parsed_TOML.get_data())

    # When the request method is GET, checks if there is already a database containing
    # visualizable data and returns a page containing the data visualized. If there is 
    # no prior poetry.lock upload, redirects the user to mainpage.
    elif request.method == "GET":
        if hasattr(after_file_upload, "parsed_TOML"):
            if after_file_upload.parsed_TOML.get_data() != None:
                return render_template("index.html", value=after_file_upload.
                                                        parsed_TOML.get_data())

            else:
                return render_template("upload.html")
        else:
            return render_template("upload.html")

@app.route("/data", methods=["GET", "POST"])
def depency_clicked():
    """Function which contains the logic to visualize a single depency and its
    depencies and reversedepencies in the project.
    """

    if request.method == "POST":
        name = request.form["name"]

        package = after_file_upload.parsed_TOML.get_data()[name]

        # Split the packages depencies to installed and not installed for 
        # visualizing purposes
        installed_depencies = []
        not_installed_depencies = []
        for depency in package.get_depencies():
            if(depency.get_installed()):
                installed_depencies.append(depency)
            else:
                not_installed_depencies.append(depency)

        # Split the packages reverse depencies to installed and not installed
        # for the same reason as above
        installed_rev_depencies = []
        not_installed_rev_depencies = []
        for rev_depency in package.get_reverse_depencies():
            if(rev_depency.get_installed()):
                installed_rev_depencies.append(rev_depency)
            else:
                not_installed_rev_depencies.append(rev_depency)

        return render_template("data.html", name=package, 
            desc=package.get_desc(), ins_dep=sorted(installed_depencies),
            not_ins_dep=sorted(not_installed_depencies), 
            ins_rev_dep=sorted(installed_rev_depencies),
            not_ins_rev_dep=sorted(not_installed_rev_depencies))

    # Redirect GET requests to the mainpage
    elif request.method == "GET":
        return render_template("upload.html")
        