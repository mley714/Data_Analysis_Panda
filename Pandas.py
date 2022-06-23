# Define a Pandas Series with a default index
import pandas as pd
my_list =['NVDA', 'MSFT', 'META', 'AMZN', 'UNH']
my_list
# print(type(my_list))
# print(my_list)

series_1 = pd.Series(data=my_list)
print(series_1)
type(series_1)

series_2 = pd.Series(data=[100,200,500,1000,5000])
print(series_2)

my_series=pd.Series(['gf', 'star wars', 'wall street'])
print(my_series)
print(type(my_series))