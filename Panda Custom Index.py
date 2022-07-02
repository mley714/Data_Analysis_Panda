import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

my_list=['NVDA', 'MSFT', 'UNH', 'AAPL', 'META']
print(my_list)
my_labels=['stock#1', 'stock#2', 'stock#3', 'stock#4', 'stock#5']
series_3 =pd.Series(data=my_list, index=my_labels)

print(type(series_3))
print(series_3)
