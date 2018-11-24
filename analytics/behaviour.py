from utils import *
from sklearn.cluster import DBSCAN

#dbscan with fixed epsilon and min samples to detect outliers in dataset
def db_scan(data, eps, min_samples):
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(data)
    num_dbscan = len(np.unique(db.labels_))
    return db.labels_, num_dbscan

#This will get all values to corresponding integets and return as a numpy array
def pre_process(df):
    return df.replace({'Mood': mood_dict_inverted, 'Location': location_dict, 'Time':time_dict}).values[:,1:]

#this method will generate data and return any unusual behaviour
def unusual_behaviour(data_set):
    #process to numerical data for clustering techniques
    numerical_data = pre_process(data_set)
    #labels are what catagory emotion log fills, where -1 indicates no catagory
    #num labels indicates the number of catagories for emotion logs
    labels, num_labels = db_scan(numerical_data, 1.5, 5)
    #find emot logs that have label -1
    outliers = np.where(labels == -1)[0]
    return data_set.loc[outliers]

def emotion_by_location(data_set):
    location_options = ['Home', 'Gym', 'Library', 'Class', 'Bar']
    data_set = data_set.replace({'Mood': mood_dict_inverted})
   
    #emotion values for logs recorded at each location
    home_values = data_set.loc[data_set['Location'] == 'Home']['Mood'].values
    gym_values = data_set.loc[data_set['Location'] == 'Gym']['Mood'].values
    lib_values = data_set.loc[data_set['Location'] == 'Library']['Mood'].values
    class_values = data_set.loc[data_set['Location'] == 'Class']['Mood'].values
    bar_values = data_set.loc[data_set['Location'] == 'Bar']['Mood'].values

    avg_home = round(np.mean(home_values), 2)
    avg_gym = round(np.mean(gym_values), 2)
    avg_lib = round(np.mean(lib_values), 2)
    avg_class = round(np.mean(class_values), 2)
    avg_bar = round(np.mean(bar_values), 2)

    return avg_home, avg_gym, avg_lib, avg_class, avg_bar



if __name__ == '__main__':
    data_set = gen_mood(100)
    weirdness = unusual_behaviour(data_set)
    print(weirdness)

    emotion_by_location(data_set)
