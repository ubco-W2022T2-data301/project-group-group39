import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_process(url_or_path_to_csv_file): 
    df1 = (
    pd.read_csv(url_or_path_to_csv_file)
    )
    
    df2 = (
        df1
        .groupby('season')
        .apply(lambda x: x.nlargest(10, 'pts')
        .mean(numeric_only=True))
        .reset_index()[['season', 'pts']] 
    )
    
    return df2
