# preprocess.py
# preprocess.py: This script preprocesses the data in the rawsettlement.csv file.

import pandas as pd
from utils import load_data, save_data, drop_columns, rename_columns, get_column_datatypes

def preprocess(rawsettlement_file, processed_file):
    # Load data
    df = load_data(rawsettlement_file)

    # Define columns
    columns = ['ReplacementPrice','ReplacementPriceReferenceVolume','TotalAcceptedOfferVolume','TotalAcceptedBidVolume','TotalAdjustmentSellVolume','TotalAdjustmentBuyVolume','TotalSystemTaggedAcceptedOfferVolume','TotalSystemTaggedAcceptedBidVolume','TotalSystemTaggedAdjustmentSellVolume','SellPriceAdjustment','BuyPriceAdjustment','PriceDerivationCode','ReserveScarcityPrice','TotalSystemTaggedAdjustmentBuyVolume','SystemSellPrice','BsadDefaulted']

    # Drop columns
    df = drop_columns(df, columns)
    
    # Rename columns
    columns_to_rename = {'SystemBuyPrice': 'Price'}
    df = rename_columns(df, columns_to_rename)
    
    # Save data
    save_data(df, processed_file)

    
    
if __name__ == '__main__':
    rawsettlement_file = '/Users/julieagwu/Library/Mobile Documents/com~apple~CloudDocs/GB Power Market/Settlement Data/data/rawsettlement.csv'
    processed_file = '/Users/julieagwu/Library/Mobile Documents/com~apple~CloudDocs/GB Power Market/Settlement Data/data/processed_data.csv'
    preprocess(rawsettlement_file, processed_file)
    
    print('Data preprocessing complete.')
