import pandas as pd
import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt

# Method chaining begins

def cleaned_data(path):
    df1 = (
    pd.read_csv(path,parse_dates=True)
    .dropna(how='any')
    .drop_duplicates())
        
    df2 = df.copy().drop(['time','Ground','Summary','Location',"Unnamed: 11","Unnamed: 12"],axis=1)
    return df2
    

def loadData(path):
    df=pd.read_csv(path,parse_dates=True)
    def describe_dataset():
        return data.describe

    def loadAlive():
        return [df['Aboard']-df['Fatilities']

            
def data_clean(path):
    data_ = pd.read_csv(path,parse_dates=True).dropna(how='any').drop_duplicates()
 
    return data_