

import pandas as pd

def file_Loading(path):
   
    # Method Chain 1 (Load data, drop na rows, drop unneeded columns)
    
    # Preparing list needed
    drop_columns = ['registeration','Ground','Location','time']
    def clean_file:
        df1 = (pd.read_csv("/Users/raghavbhagria/Desktop/COSC301/project-group46/data/processed/processed.csv").dropna().drop(drop_columns, axis=1).reset_index(drop=True))
        
    def rename_col:
        df2=df1.rename(columns={'Fatilities':'Deaths'}, inplace=True)
    
    return df2