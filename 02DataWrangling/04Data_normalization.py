#simple feature scaling 
df["length"] = df["length"]/ df["length"].max()

#min-max
df["length"] = (df["length"]-df["length"].min())/(df["length"].max-df["length"].min())

#z-score
df["length"] = (df["length"]-df["length"].mean())/df["length"].std()