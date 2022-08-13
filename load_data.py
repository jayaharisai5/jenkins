# import required libraries
import pandas as pd


# importing the data
def load_data():
    data = pd.read_csv("survey lung cancer.csv")  # loading the dataset to dataframe
    #print(data)
    return data

# calling the function
#load_data()
