from flask import Flask, jsonify, request, render_template,redirect,url_for
import random
import datetime

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

@app.route("/updateTempHum")
def updateHum():
    return jsonify(str(random.randint(0,100)))

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