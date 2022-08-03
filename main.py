from asyncio.log import logger
from urllib import response
from flask import Flask, request, Response, redirect, url_for, jsonify
from marshmallow import fields, Schema
import os
import werkzeug.utils
from flask_pymongo import PyMongo
import pymongo
import datetime
import smtplib, ssl
from json import loads
from bson.json_util import dumps



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://@cluster0.wlxrg.mongodb.net/cough?retryWrites=true&w=majority"
mongo = PyMongo(app)

id = 0
global data_object
data_object = {}

class Data(Schema):
    workstation = fields.String(required = True)
    cough_count = fields.Integer (required = True)
    temperature = fields.Float(required = True)
    last_updated = fields.DateTime(required = True)

#app_root = os.path.dirname(os.path.abspath(__file__))



@app.route('/home', methods = ['POST'] )
def getData():
    audio = os.path.join("Audio.wav")
    request.files["upload_file"].save(audio)
    temp = request.form['temperature']
    global tempfloat
    tempfloat = float(temp)
    sendemail(tempfloat)
    now = datetime.datetime.now()
    data_object = {
        "last_updated":now.strftime("%Y-%m-%d %H:%M:%S"),
        "workstation": "1",
        "cough_count": 2, 
        "temperature": temp
        }
    userdata = mongo.db.usercollection.insert_one(Data().load(data_object)).inserted_id
    data = mongo.db.usercollection.find_one(userdata)
    return Response(data, status = 200)
    
@app.route('/user', methods = ['GET'] )
def getUserData():
    users = mongo.db.usercollection.find()
    return jsonify(loads(dumps(users))), 200


#SEND EMAIL
def sendemail(tempfloat):
    sender_email = ''
    email_password = ''
    receiver_email = ''

    if (tempfloat >38):
        message = """Workstation: 1
        Reported for having : High temperature
        Body temperature: {} C""".format(tempfloat)
    
        port = 465  
        app_password = email_password
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("@gmail.com", app_password)
            server.sendmail(sender_email, receiver_email, message)


if __name__ == '__main__':
    app.run(debug=True, port=3000, host ="")
