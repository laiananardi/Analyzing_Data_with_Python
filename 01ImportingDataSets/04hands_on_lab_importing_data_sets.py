# Import pandas library
import pandas as pd
import numpy as np

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
print(df.head(5))

# Write your code below and press Shift+Enter to execute 
print("The last 10 rows of the dataframe\n")
print(df.tail(10))

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

#eplace headers and recheck our dataframe
df.columns = headers
print(df.head(10))


df1 = df.replace('?',np.NaN)

df=df1.dropna(subset=["price"], axis=0)
print(df.head(20))

df.to_csv("automobile.csv", index=False)


# Data Formate	Read	Save
# csv	pd.read_csv()	df.to_csv()
# json	pd.read_json()	df.to_json()
# excel	pd.read_excel()	df.to_excel()
# hdf	pd.read_hdf()	df.to_hdf()
# sql	pd.read_sql()	df.to_sql()
# ...	...	...


# check the data type of data frame "df" by .dtypes
print(df.dtypes)

# describe all the columns in "df" 
print(df.describe(include = "all"))