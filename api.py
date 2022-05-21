from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from TOML_Parser import TOML_Parser
import os

app = Flask(__name__)

@app.route("/")
def upload_file():
    return render_template("upload.html")

@app.route("/index", methods=["GET", "POST"])
def after_file_upload():
    if request.method == "POST":
        file = request.files["file"]
        file.save(secure_filename(file.filename))
        
        after_file_upload.parsed_TOML = TOML_Parser(
            secure_filename(file.filename))

        os.remove(secure_filename(file.filename))

        if after_file_upload.parsed_TOML.get_data() == None:
            return render_template("upload.html", error="Please upload a .lock file")

        return render_template("index.html", 
            value=after_file_upload.parsed_TOML.get_data())

    elif request.method == "GET":
        return render_template("upload.html")

@app.route("/data", methods=["GET", "POST"])
def depency_clicked():
    if request.method == "POST":
        name = request.form["name"]

        package = after_file_upload.parsed_TOML.get_data()[name]

        installed_depencies = []
        not_installed_depencies = []
        for depency in package.get_depencies():
            if(depency.get_installed()):
                installed_depencies.append(depency)
            else:
                not_installed_depencies.append(depency)

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

    elif request.method == "GET":
        return render_template("upload.html")



if __name__ == "__main__":
    app.run(debug=True)
    