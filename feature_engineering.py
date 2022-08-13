from sys import implementation
from load_data import load_data         #importing the function from the another python file load_data.py

def feature_engineering():
    data_frame = load_data()
    
    #finding the duplicate values from the data_frame
    duplicate = data_frame[data_frame.duplicated()]
    #print(duplicate.index)       
    #index values of the diplicates
    #removing the duplicates
    #print(data_frame.shape)             #checking the shape of the data frame before
    for i in duplicate.index:
        print( "index ", i, " is removed and no longer available")
        data_frame.drop(index=[i], inplace = True)
        data_frame.reset_index()                #resetting the index values
    #print(data_frame.shape)             #checking the shape of the dataframe after removing the duplicates
    #feature engineering the GENDER, LUNG_cancer features 
    data_frame.replace({'GENDER':{'F':0,'M':1}},inplace=True)
    data_frame.replace({'LUNG_CANCER':{'YES':0,'NO':1}},inplace=True)

    #print(data_frame.head())  #here you can see the features are convereted by printing
    return data_frame
#feature_engineering()