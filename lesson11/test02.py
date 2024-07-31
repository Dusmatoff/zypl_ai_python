import pandas as pd
import datetime

data = pd.read_csv("../purchases.csv", sep=";")
# data2 = pd.read_excel("../purchases.csv")
data["summa"] = data["price"] * data["volume"]
data["summa"] = data["summa"].map(lambda x: round(x, 2))

data_without_nan = data.dropna()
data["date"].fillna(datetime.date.today(), inplace=True)
#data.to_excel("purchases_new.xlsx")
print(data)
