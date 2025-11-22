# ETL pipeline for machine learning
import os
import json
from pathlib import Path
import pandas as pd

def extract(folder:str) -> pd.DataFrame:
    """
    Extract takes in a folder of json,csv's, and parquet
    files and saves them as a pandas dataframe 
    """
    dataframes = []
    for file in os.listdir(folder):
        path = os.path.join(folder,file)
        if file.endswith('.csv'):
            df = pd.read_csv(path)
        elif file.endswith('parquet'):
            df = pd.read_parquet(path)
        else:
            df = pd.read_json(path, lines=True)
        print(f"loaded {file} of shape : {df.shape}")
        dataframes.append(df)
    
    # concatenates all dataframes to one
    data = pd.concat(dataframes, ignore_index=True)
    return data

if __name__ == "__main__":
    folder = "data/"
    data = extract(folder=folder)
    print(data.head())