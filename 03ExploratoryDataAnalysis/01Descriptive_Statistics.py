#Summarize statistics using pandas describe()
df.describe()
 
#Summarize the categorical data by using the value_counts() method

dw = df["drive-wheels"].value_counts().to_frame()
dw.rename(columns= {'drive-wheels':'value_counts'}, inplace=True)

#Box Plot

sns.boxplot(x='drive-wheels', y='price', data=df)