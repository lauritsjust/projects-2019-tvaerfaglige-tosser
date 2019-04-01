def fetch_data(tickers):
    # Import neccesary modules and packages #
    import pandas as pd
    import matplotlib.pyplot as plt

    # SET ATTRIBUTES FOR DATA FETCH #
    apikey = "XU0S88ZM101LB0FQ" 
    outputsize = "full" # Compact or full, if daily data. Compact is 100 days, full is 20+ years.
    freq = "DAILY" # DAILY, WEEKLY OR MONTHLY

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