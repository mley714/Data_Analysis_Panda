import pandas as pd
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
# Get historical data

raw_csv_data =pd.read_csv("foods.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
df = raw_csv_data.copy()
# print(df)


Stock = "AAPL"
data = yf.download(Stock, start="2022-06-01",end="2022-06-22")
data.tail(5)
print(data)