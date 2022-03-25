#from crypt import methods
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import pyrebase as pb
import json

app = Flask(__name__)
CORS(app)
# sqlalchemy

# dialect+driver://username:password@host:port/database

firebaseConfig = {
  "apiKey": "AIzaSyCCD_YMl1GVhCacEWtj424cMrmqHWqyzw0",
  "authDomain": "jobmicroservice-13a0c.firebaseapp.com",
  "databaseURL": "https://jobmicroservice-13a0c-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "jobmicroservice-13a0c",
  "storageBucket": "jobmicroservice-13a0c.appspot.com",
  "messagingSenderId": "209394015065",
  "appId": "1:209394015065:web:b6612fd69caeaea6124a48"
}

firebase = pb.initialize_app(firebaseConfig)
db = firebase.database() #user realtime db

# db.create_all()

@app.route("/jobs") # get all jobs
def get_all():
    try:
        jobs = db.child("jobs").get()
        jobsDict = {}        
    
        for job in jobs.each():
            print(type(job.key()))
            print("___________") 
            print("key:",job.key())
            print("value:",job.val())
            jobsDict[job.key()] = job.val()
        print("Job dict:",jobsDict)
        # return userDict
        # return json.dumps(jobsDict) #return all user data
        return jsonify(
                    {
                        "code": 201,
                        "data": json.dumps(jobsDict)
                    }
                    ), 201
    
    except Exception as e:
        # print(e)

        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while getting the jobs. " + str(e)
            }
        ), 500

@app.route("/jobs/create",methods = ["POST"])
def post_job():
    try:
        data = request.data.decode("utf-8") #decode bytes --> data received is in bytes; need to decode 
        data = json.loads(data)
        print(type(data))
        data["posted_timestamp"] = str(datetime.now())
        db.child("jobs").push(data)

        return jsonify(
            {
                "code": 201,
                "data": data
            }
            ), 201

    except Exception as e:
        # print(e)

        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the job. " + str(e)
            }
        ), 500
    

@app.route("/jobs/<string:JobID>")
def get_job_by_id(JobID):
    try:
        job = db.child("jobs/"+JobID).get()
        jobDict = {}

        jobDict[job.key()] = job.val()
        print(jobDict[JobID])
        # print(user.key())
        print(bool(jobDict[JobID])) #return true and false
        
    # bool(userDict["users"])

        if(bool(jobDict[JobID])): #yes theres an existing user
            result = json.dumps(jobDict)
            return jsonify(
                {
                    "code": 201,
                    "data": result
                }
                ), 201
            # return "404"  #empty user valu
        return jsonify(
            {
                "code": 400,
                "data": "The user value is empty"
            }
        ), 400

    except Exception as e:
        # return "NOT OK"
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while finding the jobs. " + str(e)
            }
        ), 500

@app.route("/update_vacancy/<string:JID>",methods = ["PUT"]) # update vacancy
def update_vacancy(JID):
    try:
        # data = request.data.decode("utf-8") #decode bytes --> data received is in bytes; need to decode 
        # data = json.loads(data)
        print('jobs/'+JID+'/vacancy')
        getGivenJob = db.child('jobs/'+JID).get()
        givenJobDict = {}        
                
    
        for field in getGivenJob.each():
            print(type(field.key()))
            print("___________") 
            print("key:",field.key())
            print("value:",field.val())
            givenJobDict[field.key()] = field.val()
        print(givenJobDict)
        vacancy = givenJobDict["vacancy"]
        # return vacanciesDict

        if(vacancy > 0):
            updated_v = vacancy-1
            db.child("jobs/"+JID).update({"vacancy":updated_v})
            return str(updated_v)
        else:
            return "500"
        # return decision
    except Exception as e:
        # print(e)

        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while updating vacancy. " + str(e)
            }
        ), 500

if __name__ == "__main__":
    app.run(port = 5001,debug = True)