import numpy as np
import pandas as pd


'''
Daily mood is modelled by a 1 step Markov process, period 1 day 
Location is modelled by a i.i.d process, distributed in favour of home, library, class, gym, bar
Time is modelled by uniform i.i.d process over options
Pass method number of days to generate data for
'''
def gen_mood(days):
    #mood options
    mood_options = [-2, -1, 0, 1, 2]
    #transition probabilities
    mood_transition = np.array([[0.4, 0.4, 0.2, 0.0, 0.0],
                                [0.1, 0.4, 0.4, 0.1, 0.0],
                                [0.0, 0.1, 0.6, 0.3, 0.0],
                                [0.0, 0.0, 0.4, 0.4, 0.2],
                                [0.0, 0.0, 0.2, 0.4, 0.4]])
    #location options
    location_options = ['Home', 'Gym', 'Library', 'Class', 'Bar']
    #probablities for each option
    location_probabilities = [0.4, 0.1, 0.2, 0.2, 0.1]
    #time options
    time_options = ['09AM', '10AM', '11AM', '12PM', '01PM', '02PM', '03PM', '04PM', '05PM', '06PM', '07PM', '08PM']


    #time series list for moods 
    mood_time_series = []
    #time series list for locations
    location_time_series = []
    #time series list for time of requests
    request_time = []

    #init starting mood to be happy :) 
    current_mood = 4

    #randomly choose for each day
    for _ in range(days):
        #append new mood to list by probabilites for current state
        mood_time_series.append(np.random.choice(a=mood_options, p=mood_transition[current_mood]))
        #set current mood to be whatever state we just landed on
        current_mood = np.where(mood_options == mood_time_series[-1])[0][0]
        #choose and append location
        location_time_series.append(np.random.choice(a=location_options, p=location_probabilities))
        #choose and apppend time of input
        request_time.append(np.random.choice(a=time_options))


    mood_data = pd.DataFrame(
        {'Day': range(days),
         'Mood': mood_time_series,
         'Time': request_time,
         'Location': location_time_series
        }).replace({'Mood': mood_dict})
    
    return mood_data

'''
Dictionaries for analysis
We require numerical values for clustering techniques, so here are invertble mappings
for each data frame parameter to a integer.
'''
#Dictionary to map mood integers to strings
mood_dict = {
    -2: "Hella Sad",
    -1: "Sad",
    0: "Neutral",
    1: "Happy",
    2: "FUCK YES" 
} 

#Location dictionary
location_dict = {
    "Home": 0,
    "Gym": 1,
    "Library": 2,
    "Class": 3,
    "Bar": 4
}

#Time Dictionary
time_dict = {
    "09AM": -3,
    "10AM": -2,
    "11AM": -1,
    "12PM": 0,
    "01PM": 1,
    "02PM": 2,
    "03PM": 3,
    "04PM": 4,
    "05PM": 5,
    "06PM": 6,
    "07PM": 7,
    "08PM": 8
}

#Inverted dictionary to map strings to integers
mood_dict_inverted = {i: j for j, i in mood_dict.items()}
location_dict_inverted = {i: j for j, i in location_dict.items()}
time_dict_inverted = {i: j for j, i in time_dict.items()}


#load sample data previously generated
def load_history():
    return pd.read_pickle('file_name')