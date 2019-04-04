#########################################
# THIS FILE IS NOT USED FOR THE PROJECT #
#########################################

# EXAMPLE LINK: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=XU0S88ZM101LB0FQ&datatype=csv

# Import neccesary modules and packages #
import pandas as pd
import matplotlib.pyplot as plt

# SET ATTRIBUTES FOR DATA FETCH #
apikey = "XU0S88ZM101LB0FQ" 
outputsize = "full" # Compact or full, if daily data. Compact is 100 days, full is 20+ years.
tickers = ["MSFT","AAPL","AIG"] # Maximum of five stocks per data fetch and only one data fetch per minute allowed
freq = "DAILY" # DAILY, WEEKLY OR MONTHLY
adjusted_close = True

# Empty Panda DataFrame to append individual stock data to 
stocks_df = pd.DataFrame() 

# Loop through tickercodes and fetch data individually, then append to stocks_df
for ticker in tickers:
    fetch_link = "https://www.alphavantage.co/query?function=TIME_SERIES_" + freq + "_ADJUSTED&symbol=" + ticker + "&outputsize=" + outputsize + "&apikey=" + apikey + "&datatype=csv"
    df = pd.read_csv(fetch_link)
    df["ticker"] = ticker
    print("Mean close for " + ticker +  " is " + str(round(df.close.mean(),2)))
    stocks_df = stocks_df.append(df,ignore_index=True)
print("Mean close for all stocks is " + str(round(stocks_df.close.mean(),2)))
print("\n-----------------------------------\n")
#Vi laver nu en graf der viser udviklingen
days = 1000
for ticker in tickers:
    get_stock=stocks_df.loc[stocks_df['ticker'] == ticker, :]
    get_stock=get_stock.iloc[0:days]
    get_stock = get_stock[::-1] # Reverses order of dataframe
    get_stock = get_stock.reset_index() # Re-indexes
    plt.plot(get_stock['timestamp'], get_stock['adjusted_close'] if adjusted_close == True else get_stock['close'])
    plt.title(ticker)
    # HERUNDER LAVES X-AKSEN
    #SLET IKKE DENNE KOMMENTAR: first_day_of_month = stocks_df.loc[get_stock['timestamp'].str[-2:] == "01", :].index.tolist()
    if (days <= 180):
        every_x_day = round(days/22+0.5)
        trading_days = get_stock.iloc[0:days].index.tolist()
        ticks = trading_days[::every_x_day]
        timestamp_values = get_stock["timestamp"][ticks] 
    elif (days <= 180):
        first_trading_day_of_month = get_stock.loc[get_stock['timestamp'].str[-2:] < get_stock['timestamp'].str[-2:].shift(periods=1),:].index.tolist()
        ticks = first_trading_day_of_month
        timestamp_values = get_stock["timestamp"].str[:7][ticks]
    else:
        first_trading_day_of_year = get_stock.loc[get_stock['timestamp'].str[:4] > get_stock['timestamp'].str[:4].shift(periods=1),:].index.tolist()
        ticks = first_trading_day_of_year
        timestamp_values = get_stock["timestamp"].str[:4][ticks]
    plt.xticks(ticks,timestamp_values)
    plt.xticks(rotation=75)
    plt.show()