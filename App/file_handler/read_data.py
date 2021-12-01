"Read data from csv file"
import pandas as pd

def read_data(test_data_path):
    "Read data from csv file"
    data= pd.read_csv(test_data_path)
    data_frame = pd.DataFrame(data, columns=['Value 1','Value 2','Value 3','Result'])
    return data_frame
