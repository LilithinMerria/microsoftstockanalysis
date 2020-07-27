import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

microsoft = pd.read_csv("D:\DataAnalytics\MicrosoftStockMarket\MSFT.csv", index_col=0)
#print(microsoft.shape)
#print(microsoft.describe())
micro_july = microsoft.loc["2019-07-05": "2019-07-11"]
print(micro_july)
print(micro_july.loc["2019-07-08"])
#print(microsoft.iloc[1, 2])

#range of july
micro_july_m = microsoft.loc["2019-07-01": "2019-07-31"] 

#create pricediff column of Close 
microsoft["PriceDiff"] = microsoft["Close"].shift(-1) - microsoft["Close"] 
microsoft["DailyReturn"] = microsoft["PriceDiff"] / microsoft["Close"]

# create direction column using list comprehension, moving average(s), profit, etc ...
microsoft["Direction"] = [1 if microsoft["PriceDiff"].loc[i] > 0 else 0 for i in microsoft.index]
microsoft["MovingAverage10"] = microsoft["Close"].rolling(10).mean()
microsoft["MovingAverage50"] = microsoft["Close"].rolling(50).mean()
microsoft = microsoft.dropna()
microsoft["Close1"] = microsoft["Close"].shift(-1)
microsoft["Shares"] = [1 if microsoft.loc[i, "MovingAverage10"] > microsoft.loc[i, "MovingAverage50"] else 0 for i in microsoft.index]
microsoft["Profit"] = [microsoft.loc[i, "Close1"] - microsoft.loc[i, "Close"] if microsoft.loc[i, "Shares"] == 1 else 0 for i in microsoft.index]
#print(microsoft["PriceDiff"].loc["2019-07-08"]) 
print(microsoft.head(5))

# Plot Profit
microsoft["Profit"].plot()
plt.axhline(y=0, color="red")
plt.show()

# Calculating accumulated wealth using cumsum method
microsoft["Wealth"] = microsoft["Profit"].cumsum()
print(microsoft.tail(5))

# Plot Wealth accumulated
microsoft["Wealth"].plot()
plt.title("Total money gained is {}".format(microsoft.loc[microsoft.index[-2], "Wealth"]))
plt.show()


#plt.figure(figsize=(12,7))
#microsoft["Close"].plot(label="Close")
#microsoft["MovingAverage50"].loc["2019-07-01": "2020-08-20"].plot(label="MovingAverage50")
#plt.legend()
#plt.show()

#microsoft["High"].plot()
#plt.show()
#micro_july_m["Close"].plot()
#plt.show()
