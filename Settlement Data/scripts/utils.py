#utils.py: This file contains utility functions that are used in the main preprocess.py script.
import pandas as pd

def load_data(rawsettlement_file):
    return pd.read_csv(rawsettlement_file)

def save_data(df, file_path):
    df.to_csv(file_path, index=False)
# The load_data function reads a CSV file and returns a pandas DataFrame object.
# The save_data function saves a pandas DataFrame object to a CSV file.
# These functions are used in the main preprocess.py script to load and save data.
def drop_columns(df, columns):
    return df.drop(columns=columns, axis=1)
    columns = ['ReplacementPrice,ReplacementPriceReferenceVolume','TotalAcceptedOfferVolume','TotalAcceptedBidVolume','TotalAdjustmentSellVolume','TotalAdjustmentBuyVolume','TotalSystemTaggedAcceptedOfferVolume','TotalSystemTaggedAcceptedBidVolume','TotalSystemTaggedAdjustmentSellVolume', 'SystemSellPrice']
    
def rename_columns(df, columns):
    return df.rename(columns=columns)
    columns = {'SystemBuyPrice': 'Price'}
    
#return datetype of each column as a dataframe

def get_column_datatypes(df):
    return df.type()

print('utils.py loaded')