# ETL pipeline for machine learning
import os
import json
from pathlib import Path
import pandas as pd
import sqlite3

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


def transform(df:pd.DataFrame):
    #fuction takes in the dataframe from the extract function
    print('transformation processing...')
    print('-'*15)
    print('cleaning data...')
    df.columns = df.columns.str.lstrip()
    df = df.rename(columns={'Label':'attack'})
    df['attack'] = df['attack'].apply(lambda x: 1 if "dos" in str(x).lower() else 0 )
    print('filtering data...')
    df['f_b_total_packet_ratio'] =  df['Total Backward Packets'] / (1 + df['Total Length of Fwd Packets'])
    wanted = ['f_b_total_packet_ratio', 'Fwd Packet Length Max', 'Bwd Packet Length Std', 'Flow IAT Mean', 'act_data_pkt_fwd']
    x = df[wanted].copy()
    y = df['attack'].copy()
    return x,y
    
    


def load(x:pd.DataFrame, dbname:str, tableName:str):
    #takes in a pandas dataframe which will be loaded to sqlite database
    sqlconnection = sqlite3.connect(dbname)
    
def ETL(folder:str, dbname:str,):
    df = extract(folder=folder)
    x,y = transform(df=df)
    db_name = 'machine_learning_training_data'
    load(x, dbname=dbname, tableName='training_data_xtrain')   
    load(y, dbname=dbname, tableName='training_data_ytrain') 
    
    
if __name__ == "__main__":
    folder = "data/"
    data = extract(folder=folder)
    print(data.head())
    
