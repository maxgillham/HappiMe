import numpy as np



'''
Modelling daily mood by a 1 step Markov process, period 1 day 
Pass method number of days to generate data for
'''
def gen_mood(days):
    #mood options
    mood_options = np.array([-2, -1, 0, 1, 2])
    #transition probabilities
    mood_transition = np.array([[0.4, 0.4, 0.2, 0.0, 0.0],
                                [0.1, 0.4, 0.4, 0.1, 0.0],
                                [0.0, 0.1, 0.6, 0.3, 0.0],
                                [0.0, 0.0, 0.4, 0.4, 0.2],
                                [0.0, 0.0, 0.2, 0.4, 0.4]])

    #time series list for moods 
    mood_time_series = []
    #init starting mood to be happy :) 
    current_mood = 4

    #randomly choose for each day
    for _ in range(days):
        #append new mood to list by probabilites for current state
        mood_time_series.append(np.random.choice(a=mood_options, p=mood_transition[current_mood]))
        #set current mood to be whatever state we just landed on
        current_mood = np.where(mood_options == mood_time_series[-1])[0][0]

    return mood_time_series

if __name__ == '__main__':
    mood_time_series = gen_mood(100)
    print(mood_time_series)