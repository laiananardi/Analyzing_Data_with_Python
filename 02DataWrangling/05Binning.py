import pandas as pd
import numpy as np

other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
df.replace('?', np.nan, inplace=True)
df.dropna(subset=["price"], axis=0, inplace=True)
df["price"] = df["price"].astype(int)

#binning
bins = np.linspace(min(df["price"]), max(df["price"]), 4)
group_names = ["low", "medium", "high"]
df["price-binned"] = pd.cut(df["price"],bins, labels=group_names, include_lowest=True)

print(df)