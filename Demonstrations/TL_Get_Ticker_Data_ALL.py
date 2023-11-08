# Function to get ticker data #
# T. Lockman
# September 2018
# tH3 p@cK3T$ n3v3r li3 #

from pandas_datareader import data as datas
import pandas as pd
from datetime import datetime
import csv

def hist_daily_change_list(ticker): #syear,smonth,sday,eyear,emonth,eday):
    #data = pdr.get_data_yahoo(symbols=ticker) #start=datetime(syear, sday, smonth), end=datetime(eyear, eday, emonth))
    panel_data = datas.DataReader(ticker)
    print(panel_data)
    data = panel_data.values.tolist()
    # AdjClose = (data['Adj Close'])
    # StartPrice = AdjClose[-1]
    # Low = (data['Low'])
    # High = (data['High'])

    #return {'Ticker': ticker, 'ClosePrice': StartPrice}
    return data


if __name__ == '__main__':

    # namelist = [['open','high','low','close']]
    # with open('tickerdata.csv', 'w') as f:
    #     write = csv.writer(f)
    #     write.writerows(namelist)
    # get_ticker_user = input("Please enter ticker: ")
    get_ticker_user = 'tsla'
    dataframe = (hist_daily_change_list(get_ticker_user))
    print(dataframe)
    # # dataframe = str(dataframe)
    # with open('tickerdata.csv', 'a') as f:
    #     write = csv.writer(f)
    #     write.writerows(dataframe)


        #closeprice = float(hist_daily_change_list('fnko')['ClosePrice'])
        #print(closeprice)