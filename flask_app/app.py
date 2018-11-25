from flask import *
from flask_restful import Resource, Api
import json
from datetime import datetime as dt
import requests as r
from utils import *
from behaviour import *
import io
import random
import matplotlib.pyplot as plt


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
    data_set = load_history()
    data = request.get_json('data')
    loggedDate, loggedTime = get_time()
    new_mood = data['data']['mood']
    new_location = data['data']['location']
    data_new = data_set.append({'Mood': new_mood, 'Location': new_location, 'Time': "09AM", 'Day': 100.0}, ignore_index=True)
    is_unusual = str(unusual_behaviour(data_new))
    print("Is_Unusual: " + is_unusual + ", New Mood: " + new_mood + ", New Location: " + new_location)
    return jsonify({"is_unusual": is_unusual})

@app.route('/avg_emotion_location', methods=["POST"])
def avg_emotion_location():
    data_set = load_history()
    data = request.get_json('data')
    loggedDate, loggedTime = get_time()
    new_mood = data['data']['mood']
    new_location = data['data']['location']
    data_new = data_set.append({'Mood': new_mood, 'Location': new_location, 'Time': loggedTime, 'Day': 100.0}, ignore_index=True)
    avg_home, avg_gym, avg_lib, avg_class, avg_bar = emotion_by_location(data_set = data_new)
    output = json.dumps({'Avg @ Home': avg_home, 'Avg @ Gym': avg_home, 'Avg @ Lib': avg_lib, 'Avg @ Class': avg_class, 'Avg @ Bar': avg_bar})
    return output


def get_time():
    return dt.now().strftime("%Y_%m_%d"), dt.now().strftime("%I%p")

@app.route('/home')
def home():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
