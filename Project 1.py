# EXAMPLE LINK: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=XU0S88ZM101LB0FQ&datatype=csv

# Import neccesary modules and packages #
import pandas as pd
import matplotlib.pyplot as plt
import time

# SET ATTRIBUTES FOR DATA FETCH #
apikey = "XU0S88ZM101LB0FQ" 
outputsize = "compact" # Compact or full. Compact is 100 days, full is 20+ years.
tickers = ["AAPL", "TSLA", "TEVA"] # MAX of five 

# Empty Panda DataFrame to append individual stock data to 
stocks_df = pd.DataFrame() 

# Loop through tickercodes and fetch data individually, then append to stocks_df
for ticker in tickers:
    fetch_link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=" + outputsize + "&apikey=" + apikey + "&datatype=csv" # Building each fetch link
    df = pd.read_csv(fetch_link) # Load CSV from above URL to df
    df["ticker"] = ticker # Add ticker-column for identification after appending
    print("Mean close for " + ticker +  " is " + str(round(df.close.mean(),2))) #Print mean of each, just a check
    stocks_df = stocks_df.append(df,ignore_index=True) # Append df for each stock to stocks_df
# Loop end

#Data cleaning and analysis begin
print("Mean close for all stocks is " + str(round(stocks_df.close.mean(),2))) # Print mean of all shares for check



