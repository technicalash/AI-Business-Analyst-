import pandas as pd
df=pd.read_csv("2a2823b5-abdf-4320-b7bd-ec63cd3258aa.csv")
print(df.isnull().sum())
print(df.shape)