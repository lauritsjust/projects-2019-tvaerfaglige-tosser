# EXAMPLE LINK: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=XU0S88ZM101LB0FQ&datatype=csv

# Import neccesary modules and packages #
import pandas as pd
import matplotlib.pyplot as plt
import time
import matplotlib.dates as mdates

# SET ATTRIBUTES FOR DATA FETCH #
apikey = "XU0S88ZM101LB0FQ" 
outputsize = "compact" # Compact or full. Compact is 100 days, full is 20+ years.
tickers = ["AAPL", "TSLA", "TEVA"] # Maximum of five stocks per data fetch and only one data fetch per minute allowed

# Empty Panda DataFrame to append individual stock data to 
stocks_df = pd.DataFrame() 

# Loop through tickercodes and fetch data individually, then append to stocks_df
for ticker in tickers:
    fetch_link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=" + outputsize + "&apikey=" + apikey + "&datatype=csv"
    df = pd.read_csv(fetch_link)
    df["ticker"] = ticker
    print("Mean close for " + ticker +  " is " + str(round(df.close.mean(),2)))
    stocks_df = stocks_df.append(df,ignore_index=True)
print("\nBased on aggregate dataframe:")
print("Mean close for all stocks is " + str(round(stocks_df.close.mean(),2)))
print("\n-----------------------------------\n")
print(stocks_df)
#Vi laver nu en graf der viser udviklingen
#fig = plt.figure(figsize=(10,5))
#ax = fig.add_subplot(1,1,1)
#ax.set_title('ticker_name')
#timestamp=stocks_df.loc[stocks_df['ticker'] =='AAPL', ['timestamp']]
#timestamp2=timestamp['timestamp']
#close=stocks_df.loc[stocks_df['ticker'] =='AAPL', ['close']]
#x.plot(timestamp2,close)
ax = stocks_df.plot(x_compat=True)
ax.xaxis.set_major_locator(mdates.MonthLocator())

plt.show()