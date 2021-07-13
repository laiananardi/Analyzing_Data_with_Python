import pandas as pd
# basics insights of dataset

#Pandas type, native, type, description
# object - string - numbers and strings
# int64 - int - numeric characters
# float64 - float - numeric characters with decimals
# datetime64, timedelta[ns] - N/A (but see the datetime module in python's standard library) - time data

#how to check the data type
data = {'First Column Name':  ['First value', 'Second value',...],
        'Second Column Name': ['First value', 'Second value',...],
        }

df = pd.DataFrame(data, columns = ['First Column Name','Second Column Name',...])
print(df.dtypes)