import pandas as pd

other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers

print(df.head(10))
#data pre-processing is the process of converting or mapping data from
# one raw form into
# another format to make it ready for further analysis.
# Data preprocessing is often called
# data cleaning or data wrangling,

#simple dataframe operations

# In Python, we usually perform operations along columns.
# Each row of the column represents a sample,

#You access a column by specifying the name of the column.
print(df["symboling"])

print(df["body-style"])

# Each of these columns is a Panda series.

# you can add
# a value to each entry off a column.
# To add one to each symbolling entry, use this command.

df["symboling"] = df["symboling"] + 1

print(df["symboling"])

# This changes each value of
# the Data frame column by adding one to the current value.