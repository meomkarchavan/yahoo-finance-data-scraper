import pandas as pd
def merge_pf(df1,df2):
    return df1.append(df2, ignore_index=True)

def open_csv(path):
    try:
        return pd.read_csv(path,index_col=None)
    except (FileNotFoundError, pd.errors.EmptyDataError) as _:
        return None