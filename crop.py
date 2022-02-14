

import pandas as pd

df=pd.read_csv("bristol-air-quality-data.csv",sep=';',engine='python')

df

df['Date Time'] = pd.to_datetime(df['Date Time'], format="%Y-%m-%d %H:%M")
df

df = df.loc[(df['Date Time'] >= '2010-01-01')]
df.to_csv("Crop.csv")