from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from datetime import datetime as dt
import requests as r

app = Flask(__name__)
json_data = open('patient0.json')
patient0 = json.load(json_data)

@app.route('/')
def get_data():
    return jsonify(patient0)

@app.route('/add', methods=["POST"])
def add_data():
    loggedDate, loggedTime = get_time()
    data = request.get_json('data')
    patient0[loggedDate] = {loggedTime:{}}
    patient0[loggedDate][loggedTime] = {'mood':data['data']['mood'], 'location':data['data']['location']}
    with open('patient0.json', 'w+') as f:
        json.dump(patient0, f, sort_keys=True, indent=4)
    return jsonify(patient0)

@app.route('/unusual', methods=["POST"])
def unusual():
    data = request.get_json('data')
    loggedDate, loggedTime = get_time()
    new_mood = data['data']['mood']
    new_location = data['data']['location']

    return 


def get_time():
    return dt.now().strftime("%Y_%m_%d"), dt.now().strftime("%I%p")

if __name__ == '__main__':
    app.run(debug=True)
