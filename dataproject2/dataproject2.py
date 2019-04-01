def download_data(ticker):
    import pandas as pd
    import matplotlib.pyplot as plt
    apikey = "XU0S88ZM101LB0FQ" 
    outputsize = "full" # Compact or full, if daily data. Compact is 100 days, full is 20+ years.
    freq = "DAILY" # DAILY, WEEKLY OR MONTHLY
    fetch_link = "https://www.alphavantage.co/query?function=TIME_SERIES_" + freq + "_ADJUSTED&symbol=" + ticker + "&outputsize=" + outputsize + "&apikey=" + apikey + "&datatype=csv"
    df = pd.read_csv(fetch_link)
    return(df)

def draw_graph(ticker,days,adjusted):
    import pandas as pd
    #%matplotlib inline
    import matplotlib.pyplot as plt
    get_stock=stocks_df.loc[stocks_df['ticker'] == ticker, :]
    get_stock=get_stock.iloc[0:days]
    get_stock = get_stock[::-1] # Reverses order of dataframe
    get_stock = get_stock.reset_index() # Re-indexes
    plt.plot(get_stock['timestamp'], get_stock['adjusted_close'] if adjusted == True else get_stock['close'])
    plt.title(ticker)
    # HERUNDER LAVES X-AKSEN
    #SLET IKKE DENNE KOMMENTAR: first_day_of_month = stocks_df.loc[get_stock['timestamp'].str[-2:] == "01", :].index.tolist()
    if (days < 90):
        every_x_day = round(days/22+0.5)
        trading_days = get_stock.iloc[0:days].index.tolist()
        ticks = trading_days[::every_x_day]
        timestamp_values = get_stock["timestamp"][ticks] 
    elif (days <= 360):
        first_trading_day_of_month = get_stock.loc[get_stock['timestamp'].str[-2:] < get_stock['timestamp'].str[-2:].shift(periods=1),:].index.tolist()
        ticks = first_trading_day_of_month
        timestamp_values = get_stock["timestamp"].str[:7][ticks]
    else:
        first_trading_day_of_year = get_stock.loc[get_stock['timestamp'].str[:4] > get_stock['timestamp'].str[:4].shift(periods=1),:].index.tolist()
        ticks = first_trading_day_of_year
        timestamp_values = get_stock["timestamp"].str[:4][ticks]
    plt.xticks(ticks,timestamp_values)
    plt.xticks(rotation=90)
    plt.show()