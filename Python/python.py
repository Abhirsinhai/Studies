import pandas as pd

def fill_nan(dataframe, method='ffill'):
    if method == 'ffill':
        dataframe.ffill(inplace=True)
    elif method == 'bfill':
        dataframe.bfill(inplace=True)
    elif method == 'mean':
        dataframe.fillna(dataframe.mean(), inplace=True)
    else:
        raise ValueError(f"Invalid method: {method}. Choose 'ffill', 'bfill' or 'mean'")
    return dataframe

df = pd.read_excel("C:\\Users\\abhir\\Desktop\\Code\\Python\\AirQuality.xlsx")
df = fill_nan(df, method='mean')