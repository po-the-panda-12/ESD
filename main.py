from flask import Flask, request, jsonify, redirect, url_for, render_template

import json
import pyrebase as pb
from invokes import invoke_http
from flask_cors import CORS, cross_origin
import os, sys
import requests

from flask_cors import CORS

import os, sys
from invokes import invoke_http
import requests


#to remove if we dont use rabbit amqp
# import amqp_setup
# import pika
#import json

app = Flask(__name__)
CORS(app)
@app.route("/")
def choose_role():
    return render_template("Role.php")

@app.route("/owner")
def owner_home():
    return render_template("Owner_Home.php")

@app.route("/dashboard.css")
def dashboard():
    return render_template("dashboard.css")

@app.route("/jquery-3.6.0.js")
def jquery():
    return render_template("jquery-3.6.0.js")

@app.route("/user")
def user_home():
    return render_template("User_Home.php")

@app.route("/create")
def create():
    return render_template("Create_Job.php")

@app.route("/apply")
def apply():
    return render_template("Apply_Job.php")

@app.route("/view")
def view():
    return render_template("View_Job.php")

<<<<<<< Updated upstream
=======
@app.route("/owner_status")
def accrej():
    return render_template("AccRej.php")

@app.route("/view_apps")
def view_apps():
    return render_template("View_Apps.php")

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
@app.route("/job/<JID>")
def job(JID):
    return render_template("One_Job.php",JID=JID)

<<<<<<< Updated upstream
=======
@app.route("/authenticate")
def authenticate():
    return render_template("authenticate.php")

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " applying for a job...")
    app.run(host="0.0.0.0", port=5010, debug=True)