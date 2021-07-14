#importing csv without a header

import pandas as pd
url = "path"
df = pd.read_csv(url, header = None)

#printing the dataframe in python

#prints the entire dataframe
df
#print the first n rows of the data frame
df.head(n)
#print the bottom n rows of the data frame
df.tail(n)

#adding headers
headers = ["1", "2", "3"]
df.colunms=headers
df.head(5)

#exporting a pandas dataframe to csv
path = "path"
df.to_csv(path)

#exporting to different formats

pd.read_csv()
pd.read_json()
pd.read_excel()
pd.read_sql()

df.to_csv()
df.to_json()
df.to_excel()
df.to_sql()
