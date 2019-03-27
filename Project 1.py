# EXAMPLE LINK: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=XU0S88ZM101LB0FQ&datatype=csv

# Import neccesary modules and packages #
import pandas as pd
import matplotlib.pyplot as plt

# SET ATTRIBUTES FOR DATA FETCH #
apikey = "XU0S88ZM101LB0FQ" 
outputsize = "compact" # Compact or full, if daily data. Compact is 100 days, full is 20+ years.
tickers = ["AAPL", "TSLA", "AIG", "FB"] # Maximum of five stocks per data fetch and only one data fetch per minute allowed
freq = "DAILY" # DAILY, WEEKLY OR MONTHLY

# Empty Panda DataFrame to append individual stock data to 
stocks_df = pd.DataFrame() 

# Loop through tickercodes and fetch data individually, then append to stocks_df
for ticker in tickers:
    fetch_link = "https://www.alphavantage.co/query?function=TIME_SERIES_" + freq + "&symbol=" + ticker + "&outputsize=" + outputsize + "&apikey=" + apikey + "&datatype=csv"
    df = pd.read_csv(fetch_link)
    df["ticker"] = ticker
    print("Mean close for " + ticker +  " is " + str(round(df.close.mean(),2)))
    stocks_df = stocks_df.append(df,ignore_index=True)
print("Mean close for all stocks is " + str(round(stocks_df.close.mean(),2)))
print("\n-----------------------------------\n")
print(stocks_df)
#Vi laver nu en graf der viser udviklingen
for ticker in tickers:
    get_stock=stocks_df.loc[stocks_df['ticker'] == ticker, :]
    get_stock = get_stock[::-1] # Reverses order
    get_stock_timestamp = get_stock['timestamp']
    get_stock_close = get_stock['close']
    plt.plot(get_stock_timestamp,get_stock_close)
    plt.title(ticker)
    #HER HAR JEG BARE LAVET TICKS PÅ 0%, 25%, 50%, 75% og 100%.
    days = get_stock_timestamp.size # Antallet af dage i timestamp
    ticks = [0, 0.25*days, 0.5*days, 0.75*days, days]
    # VI SKAL FINDE LOKATIONEN FOR FØRSTE I HVER MÅNED OG SÆTTE IND I STEDET
    # HERUNDER LAVES X-AKSEN
    plt.xticks(ticks)
    plt.show()
