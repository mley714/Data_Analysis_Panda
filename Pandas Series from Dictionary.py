import pandas as pd
# my_dict = {'Bank Client ID': 111,
#            'Bank Client Name': 'Steve',
#            'Net Worth': 3500,
#            'Years with Bank': 9}
# type(my_dict)
#
# series_4 = pd.Series(my_dict)

# my_stocks ={'AAPL': 139.00,
#             'UNH': 540.00,
#             'MSFT': 230.00}
# series_5 = pd.Series(my_stocks)
# print (series_5)
#
# my_list = ['NVDA', 'MSFT', 'UNH', 'AAPL','BA']
# my_series = pd.Series(data=my_list)
# my_series.values
# my_series.index
# my_series.dtype
# my_series.is_unique
# my_series.shape
# my_series.size

# my_series=pd.Series(data=[100,200,500,1000,5000])
# my_series
# my_series.sum()
# my_series.product()
# my_series.mean()
# my_series.head(2)
# print(my_series.tail(2))
# print(my_series.memory_usage())

# sp500 = pd.read_csv('S_P500_Prices.csv',squeeze=True) Creates Data series
sp500 = pd.read_csv('S_P500_Prices.csv',squeeze=False)  # Creates dataframe
print(sp500)
print(type(sp500))

