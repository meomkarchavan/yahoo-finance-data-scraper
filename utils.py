import pandas as pd
def merge_pf(df1,df2):
    return pd.concat([df1, df2])

def open_csv(path):
    try:
        return pd.read_csv(path,index_col=None)
    except FileNotFoundError:
        return None