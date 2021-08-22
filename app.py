from flask import Flask, jsonify, request, render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index2.html")

@app.route("/updateHum")
def updateHum():
    return jsonify(str(random.randint(0,100)))

@app.route("/updateTemp")
def updateTemp():
    return str(random.randint(0,100))

@app.route("/updateTimer")
def updateTimer():
    time = 600
    return jsonify(time)


if __name__ == "__main__":
    
    app.run(debug=True)