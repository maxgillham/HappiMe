import random
import pandas as pd
import utils
import sys


coords = [
	[-81.274306, 43.003094],
    [-81.277105, 43.008494], 
	[-81.276880, 43.006353], 
	[-81.286009, 42.999318], 
	[-81.276297, 43.005303]
]

location_mapping = {
	'Class': coords[4],
	'Bar': coords[1],
	'Home': coords[3],
	'Library': coords[2],
	'Gym': coords[0]
}

# # Gym
# [-81.274306, 43.003094]

# # bar
# [-81.277105, 43.008494], 

# # library
# [-81.276880, 43.006353], 

# # home
# [-81.286009, 42.999318], 

# # class
# [-81.276297, 43.005303], 

day_mapping = [
	'Monday',
	'Tuesday',
	'Wednesday',
	'Thursday',
	'Friday',
	'Saturday',
	'Sunday'
]

mood_mapping = {
	'FUCK YES': 5,
	'Happy': 4,
	'Neutral': 3,
	'Sad': 2,
	'Hella Sad': 1}

day_of_the_week_mapping = {
	0: 'Monday',
	1: 'Tuesday',
	2: 'Wednesday',
	3: 'Thursday',
	4: 'Friday',
	5: 'Saturday',
	6: 'Sunday'
}

def clean_data(df):
	df['Mood'] = df['Mood'].map(lambda a: mood_mapping[a])
	df['Location'] = df['Location'].map(lambda a: location_mapping[a])
	df['Day'] = df['Day'].map(lambda a: day_of_the_week_mapping[a%7])
	return df


def generate_all_data(df):

	features = []
	for index, row in df.iterrows():
		mood = row['Mood']
		time = '"' + str(row['Time']) + '"'
		coord = row['Location']
		day = '"' + str(row['Day']) + '"'
	
		features.append("""
		{
		  "type": "Feature",
		  "geometry": {
		    "type": "Point",
		    "coordinates": """ + str(coord) + """
		  	},
		  "properties": {
		    "mood": """ + str(mood) + """,
		    "day": """ + day + """,
		    "hour": """ + time + """
		  }
		}""")

	feature_list = ',\n'.join(features)

	feature_collection = """{
	  "type": "FeatureCollection",
	  "features": [ """ + feature_list + """ 
	  ]
	}"""

	with open("people_data.geojson", "w+") as f:
		f.write(feature_collection)


def condense_df(df):
	df['Mood'] = df['Mood'].map(lambda a: mood_mapping[a])

	count = df.groupby('Location')['Mood'].count()
	df = df.groupby(['Location'])['Mood'].mean()
	return df, count


def generate_overall_data(df, count):
	locations = df.index.tolist()
	coords = []
	for location in locations:
		coords.append(location_mapping[location])
	moods = df.values.tolist()
	counts = count.values.tolist()
	print(coords)

	features = []
	for i in range(len(coords)):
		mood = moods[i]
		coord = coords[i]
		count = counts[i]
	
		features.append("""
		{
		  "type": "Feature",
		  "geometry": {
		    "type": "Point",
		    "coordinates": """ + str(coord) + """
		  	},
		  "properties": {
		    "mood": """ + str(mood) + """,
		    "count": """ + str(count) + """
		  }
		}""")

	feature_list = ',\n'.join(features)

	feature_collection = """{
	  "type": "FeatureCollection",
	  "features": [ """ + feature_list + """ 
	  ]
	}"""


	with open("overview_data.geojson", "w+") as f:
		f.write(feature_collection)



if __name__ == '__main__':
	df = utils.load_history()
	overview_df = utils.load_history()
	overview_df, count = condense_df(overview_df)
	df = clean_data(df)
	generate_all_data(df)
	generate_overall_data(overview_df, count)