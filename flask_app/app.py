from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from datetime import datetime as dt

app = Flask(__name__)
json_data = open('patient0.json')
patient0 = json.load(json_data)

@app.route('/')
def get_data():
    return jsonify(patient0)

@app.route('/add', methods=["POST"])
def add_data():
    loggedTime = dt.now().strftime("%Y_%m_%d_%H:%M")
    data = request.get_json('data')
    print(data)
    patient0[loggedTime] = {'mood':data['data']['mood'], 'location':data['data']['location']}
    with open('patient0.json', 'w+') as f:
        json.dump(patient0, f, sort_keys=True, indent=4)
    return jsonify(patient0)

if __name__ == '__main__':
    app.run(debug=True)
