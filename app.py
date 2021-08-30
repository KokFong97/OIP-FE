from flask import Flask, jsonify, request, render_template, redirect, url_for
import random
import datetime
import sys
import time
import board
import adafruit_dht
import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import cv2
import os
import pickle
import numpy as np
import sklearn.linear_model as LinearRegression

# Initial the dht device, with data pin connected to:
#dhtDevice = adafruit_dht.DHT11(board.D18, use_pulseio=False)

#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#ser.flush()

# Firebase
# Fetch the service account key JSON file contents
cred = credentials.Certificate(
    'oip-project-firebase-adminsdk-9f843-845892ff2d.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://oip-project-default-rtdb.asia-southeast1.firebasedatabase.app'
})


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index2.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/clean")
def clean():
    return render_template("clean.html")


@app.route("/progressbar")
def pBar():
    return render_template("progressbar.html")


@app.route("/scanner")
def scanner():
    return render_template("scanner.html")


@app.route("/syringeDetection", methods=['POST'])
def syringeDetection():
    return("test")


@app.route("/updateTempHum", methods=['GET'])
def updateHum():
    success = False
    while not success:
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            success = True
            print ('humidity:', humidity, 'temperature', temperature_c)
            return jsonify(humid=str(humidity), temp=str(temperature_c))
        except RuntimeError as error:
            continue


@app.route('/timerML', methods=['POST'])
def timerML():
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']
    timePassed = data['timePassed']
    print(temperature)
    print(humidity)
    print(timePassed)

    cwd = os.getcwd()
    model_dir = cwd + "/linear_regression.pkl"

    sample_input = np.asarray([[float(humidity), float(timePassed)]])
    saved_model = pickle.load(open(model_dir, 'rb'))
    results = saved_model.predict(sample_input)
    print("model output: {} seconds to dry".format(results[0]))

    return(str(round(results[0])))
    
@app.route('/cleaning', methods = ['POST'])
def cleaning():
    ser.write(b"C")
    return("success")

@app.route('/drying', methods = ['POST'])
def draining():
    ser.write(b"D")
    return("success")

@app.route('/sterilizing', methods = ['POST'])
def drying():
    ser.write(b"E")
    return("success")

@app.route('/whole', methods = ['POST'])
def whole():
    ser.write(b"G")
    return("success")

@app.route('/stop', methods = ['POST'])
def stop():
    ser.write(b"S")
    return("success")


@app.route('/checkDB', methods=['POST'])
def checkDB():
    # As an admin, the app has access to read and write all data, regradless of Security Rules
    data = request.json
    guid = data['guid']
    ref = db.reference(guid)
    if (ref.get() is None):
        return "No Data in database"
    else:
        if(ref.get()["reuseCount"] < 11):
            if(ref.get()["uvTime"] < 10000):
                return("Syringe can use")
            else:
                return("Please dispose syringe as it has exceeded UV exposure time")
        else:
            return("Please dispose syringe as it has exceeded reuseCount")


@app.route('/readQR', methods=['POST'])
def readQR():
    #cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    # get the image
    result = True
    while(result):
        #_, img = cap.read()
        # cv2.imwrite("syringeImg/NewPicture.jpg",img)
        result = False
    # get bounding box coords and data
    img = cv2.imread("syringeImg/NewPicture.jpg")
    data, bbox, _ = detector.detectAndDecode(img)

    qrCode = "none"

    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        # for i in range(len(bbox)):
        #     cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
        #              0, 255), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        if data:
            print("data found: ", data)
            qrCode = data
            ref = db.reference(qrCode)
            if (ref.get() is None):
                return "No Data in database"
            else:
                if(ref.get()["reuseCount"] < 11):
                    if(ref.get()["uvTime"] < 10000):
                        return("Syringe can use")
                    else:
                        return("Please dispose syringe as it has exceeded UV exposure time")
                else:
                    return("Please dispose syringe as it has exceeded reuseCount")
    # display the image preview
    #cv2.imshow("code detector", img)

    # free camera object and exit
    # cap.release()
    # cv2.destroyAllWindows()

    return("No QR code")


if __name__ == "__main__":
    app.run(debug=True)
