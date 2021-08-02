import pandas as pd
import numpy as np

import matplotlib as plt
from matplotlib import pyplot

other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers


print(df)


df.replace('?', np.nan, inplace=True)
df.dropna(subset=["price"], axis=0, inplace=True)
df["price"] = df["price"].astype(int)

#binning
bins = np.linspace(min(df["price"]), max(df["price"]), 4)
group_names = ["low", "medium", "high"]
df["price-binned"] = pd.cut(df["price"],bins, labels=group_names, include_lowest=True)

print(df)
print(df["horsepower"])
vals = pd.to_numeric(df["horsepower"], errors='coerce')

df["horsepower"] = vals.fillna(vals.mean()) 

plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")



bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
print(bins)

group_names = ['Low', 'Medium', 'High']

df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)

df["horsepower-binned"].value_counts()

pyplot.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")