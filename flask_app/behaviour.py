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
    #if most recent log is unusual
    if labels[100] == -1: return True
    else: return False


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


def emotion_by_time(data_set):
    time_options = ['09AM', '10AM', '11AM', '12PM', '01PM', '02PM', '03PM', '04PM', '05PM', '06PM', '07PM', '08PM']
    data_set = data_set.replace({'Mood': mood_dict_inverted})

    nine_am_values = data_set.loc[data_set['Time'] == '09AM']['Mood'].values
    avgs = []
    for time in time_options:
        blah = data_set.loc[data_set['Time'] == time]['Mood'].values
        avgs.append(round(np.mean(blah),2))
    return avgs

if __name__ == '__main__':
    data_set = load_history()
    print(emotion_by_time(data_set))