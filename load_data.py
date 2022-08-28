# import required libraries
import pandas as pd
import boto3

session = boto3.Session( 
         aws_access_key_id='AKIA2LYVCCXT5J4TG5V7', 
         aws_secret_access_key='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')

client = boto3.client('s3')
path = 's3://mlops-storage/hari/survey lung cancer.csv'


# importing the data
def load_data():
    data = pd.read_csv(path)
    #data = pd.read_csv("survey lung cancer.csv")  # loading the dataset to dataframe
    #print(data)
    return data
#helollo
# calling the function
#load_data()
