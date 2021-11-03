from pandas_datareader import data as pdr
import pandas as pd



class AssetIndicesStreamer:


    def download_stock_indices(self, asset, start_day, end_day):
        try:
            df = pd.DataFrame()
            df = pdr.get_data_yahoo(asset = asset, start=start_day, end=end_day).reset_index()
        except Exception as e:
            # print("====================" + str(e) + "====================")
            print(start_day + " | " + asset + " | Asset Indices NOT ready yet")
        finally:
            return df
