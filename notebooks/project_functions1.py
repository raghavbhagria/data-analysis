import pandas as pd
import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt

# Method chaining begins

def processed_stats(path):
    data1 = (
    pd.read_csv(path,parse_dates=True)
    .dropna(how='any')
    .drop_duplicates())
        
    data2 = (
     data1.copy().drop(['type','registeration','Ground','time'], axis=1)
    .rename({"date": "Date of Crash", "Location":"Location for crash"})
    .reset_index(drop = True)
    )
    
    return data2

def planeData(path):
    data=pd.read_csv(path,parse_dates=True)
    def loadset():
        return data.describe

    def loadDeaths():
        return data['Fatilities']
    
def data_clean(path):
    data_ = pd.read_csv(path,parse_dates=True).dropna(how='any').drop_duplicates()
 
    return data_