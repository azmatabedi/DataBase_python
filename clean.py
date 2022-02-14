
import pandas as pd

df=pd.read_csv("Crop.csv")

df

UniqueSite=df['SiteID'].unique()
UniqueSite   #15
UniqueSite[0]
for site in UniqueSite:
  print(site)

UniqueLocation=df['Location'].unique()
for location in UniqueLocation:
  print(location)

df = df[df['SiteID'].notna()]
df['SiteID'].unique()
df.to_csv("Clean.csv")