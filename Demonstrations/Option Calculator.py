# Function to get ticker data #
# T. Lockman
# September 2018
# tH3 p@cK3T$ n3v3r li3 #



from Demonstrations.TL_Get_Ticker_Data_ALL import *
from Demonstrations.time_functions import *

day = dayint()
month = monthint()
year = yearint()
yearsback = year - 1
everything = 0
gaincalccounter = 0
gaincalclimit = 30
losscalccounter = 0
losscalclimit = 10


while 69 > everything:
    ticker = input(r"STOCK TICKER: ").upper()
    currentprice = float(input(r"Current Price: "))
    percent = float(input(r"Max Percent Deviation IN DECIMAL: "))
    percentmod = percent
    strike = float(input(r"Strike: "))
    contractprice = float(input(r"Contract Price: "))
    numberpurchased = float(input(r"Amount of Contracts Purchased: "))



    try:
        HistoricalData = hist_daily_change_list(ticker)

        currentprice = float(HistoricalData['ClosePrice'])

    except:
        print("ERROR ERROR ERROR!!!")
        exit()


    breakeven = strike + contractprice
    totalcost = contractprice * 100 * numberpurchased

    print("--------------------------------------------------------------------------------")
    print(str(ticker) + " @ $" + str(currentprice) + "  Strike for: " + str(strike) + " @ " + "$" + str(
        contractprice) + "  For Total Purchase of: " + "$" + str(totalcost))
    print("--------------------------------------------------------------------------------")
    print("PRICE      PERCENT CHANGE      POTENTIAL PROFIT/LOSS")
    while gaincalccounter < gaincalclimit:
        pricechange = currentprice * (1 + percentmod)
        profit = ((pricechange - strike) * 100 * numberpurchased) - totalcost
        if profit < 0 and everything == 0:
            print("--------------------***PROFIT LINE***---------------------------------")
            everything += 1
        print(str(pricechange) + "       " + str('{:.1%}'.format(percentmod)) + "            " + "$" + str(profit))
        percentmod = percentmod - .005
        gaincalccounter += 1
    print("-----------------------------------------------------------------")
    print("-----------------------------------------------------------------")

    percentmod = percent
    gaincalccounter = 0
    everything = 0



