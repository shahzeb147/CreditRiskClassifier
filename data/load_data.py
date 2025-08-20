import os
import pandas as pd
import kagglehub 


#path = kagglehub.dataset_download("wordsforthewise/lending-club")
#print("Path to dataset files:", path)

def load_lending_club_data():

    base_path = "/Users/muhammadshahzebali/.cache/kagglehub/datasets/wordsforthewise/lending-club/versions/3"
    file_path = os.path.join(base_path, 'accepted_2007_to_2018Q4.csv.gz')

    df = pd.read_csv(file_path, low_memory=False)
    return df
