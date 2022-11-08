import pandas as pd
import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt

file='/Users/sumermann/Desktop/301/project-group46/data/processed/COSC301_dataset - Sheet1.csv'
stats=pd.read_csv(file)
stats

stats=stats.dropna(how='any')
processed_stats=stats.drop_duplicates()
processed_stats

stats_final=processed_stats.copy().drop(['registeration','Ground','Location','time','route'],axis=1)
print(f'This is my final dataset for this task:')
stats_final


def planeData():
    def loadset():
        print(stats_final)
        print(stats_final.describe())

    def loadDeaths():
        print('\n')
        print(stats_final['Fatilities'])

    loadset()
    loadDeaths()
