from flask import Flask, jsonify, request, render_template,redirect,url_for
import random
import datetime
import sys
import time
import board
import adafruit_dht
import serial

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D18, use_pulseio=False)

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

@app.route("/cleaning", methods = ['POST'])
def syringeDetection():
    ser.write(b"C")
    return("success")

@app.route('/cleaning', methods = ['POST'])
def cleaning():
    ser.write(b"C")
    return("success")

@app.route('/draining', methods = ['POST'])
def draining():
    ser.write(b"D")
    return("success")

@app.route('/drying', methods = ['POST'])
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

if __name__ == "__main__":
    app.run(debug=True)
