#applyind a calculation to an entire column

import pandas as pd
import numpy as np

other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers

print(df.head(10))

df["city-mpg"] = 235/df["city-mpg"]

df.rename(columns={"city-mpg": "city-l"}, inplace=True)

print(df.head(10))

print(df["price"].tail())
# df["price"] = df["price"].dtype()
# print(df["price"])

df["price"] = df["price"].astype("int")
print(df["price"])