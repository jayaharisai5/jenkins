from feature_engineering import feature_engineering

from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split

def pre_processing():
    data_frame_copy = feature_engineering()     #importing the data from the feature_engineering.py file
    print(data_frame_copy)                         #checking the data by printing

    #diviting the required variable and depending variable
    X = data_frame_copy.drop(["LUNG_CANCER"],axis=1)      #required variable
    y = data_frame_copy.LUNG_CANCER         #dependent variable

    #oversampling the data
    over_samp =  RandomOverSampler(random_state=0)
    X_train_res, y_train_res = over_samp.fit_resample(X, y)
    #X_train_res.shape, y_train_res.shape

    print(X_train_res)
    #return(X_train_res, y_train_res)
    #splitting the data to the ring and test set
    X_train, X_test, y_train, y_test = train_test_split(X_train_res, y_train_res,test_size= 0.2, random_state = 0)
    print(X_train)
    return(X_train, X_test, y_train, y_test)
#pre_processing()
