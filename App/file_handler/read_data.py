import pandas as pd

AdditionPath = "/home/myuser/data/addition_test.csv"

def read_data(TestDataPath):
    "Read data from csv file"
    data= pd.read_csv(TestDataPath)
    df = pd.DataFrame(data, columns=['Value 1','Value 2','Value 3','Result'])
    return df

