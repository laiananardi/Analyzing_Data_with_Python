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

#these are the typical options you can consider:

#check with the data collection source

# drop the missing values.
    # drop the variable
    # drop the data entry
# how to drop missing values in python4
# axis = 0 drop the entire row
# axis = 1 drop the entire colunm

df.dropna(subset=["price"], axis=0, inplace=True)
print(df.head(10))

# replace missing data with a guess of what the data should be.
    # replace with the average 
    # replace it by frequency
    # replace it based on other functions
    # or... leave it as a missing data
# how to replace missing values in python

# will return the average of your data across a specified axis
mean = df["normalized-losses"].mean()

df["normalized-losses"].replace(np.nan, mean)

