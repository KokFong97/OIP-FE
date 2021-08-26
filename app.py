from flask import Flask, jsonify, request, render_template,redirect,url_for
import random
import datetime
import sys
import time

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

@app.route("/syringeDetection", methods = ['POST'])
def syringeDetection():
    return("test")

@app.route("/updateTempHum", methods = ['GET'])
def updateHum():
    humidity,temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,11)
    return jsonify(humid = str(humidity), temp = str(temperature))

@app.route('/timerML', methods = ['POST'])
def timerML():
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']
    timePassed = data['timePassed']
    print(temperature)
    print(humidity)
    print(timePassed)
    return(jsonify(str(random.randint(0,100))))

if __name__ == "__main__":
    app.run(debug=True)