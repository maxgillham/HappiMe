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
def unusual_behaviour():
    #generate our data set
    data_set = gen_mood(100)
    #process to numerical data for clustering techniques
    numerical_data = pre_process(data_set)
    #labels are what catagory emotion log fills, where -1 indicates no catagory
    #num labels indicates the number of catagories for emotion logs
    labels, num_labels = db_scan(numerical_data, 1.5, 5)
    #find emot logs that have label -1
    outliers = np.where(labels == -1)[0]
    return data_set.loc[outliers]




if __name__ == '__main__':

    print(unusual_behaviour())