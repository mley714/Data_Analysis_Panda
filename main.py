import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

from datetime import datetime
# Get historical data

pd.options.display.max_columns = None
pd.options.display.max_rows = None
raw_csv_data =pd.read_csv("foods.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(raw_csv_data)


Stock = "AAPL"
data = yf.download(Stock, start="2021-06-01",end="2022-06-22")
data.tail(5)
print(data)