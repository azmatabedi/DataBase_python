#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
socket.gethostname()


# In[1]:


import pandas as pd


# In[5]:


import sqlite3
import sqlalchemy


# In[4]:


import mysql.connector
import csv
import pymysql
import sqlalchemy,pyodbc,os
import pandas as pd


# In[5]:



os.getcwd()
#os.chdir('D:/onlinework/assignment task/dataset')


# In[6]:


print(os.listdir())


# In[7]:


import platform


# In[8]:


print (platform.node())


# In[9]:


pyodbc.drivers()


# In[33]:


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\ProjectsV13;"
    "Database=Database;"
    "Trusted_Connection=yes;")


# In[39]:


mysql="CREATE TABLE [table1] ([Date Time] INT NOT NULL PRIMARY KEY, [NOx] NCHAR(10) NULL, [NO2] NCHAR(10) NULL, [NO] NCHAR(10) NULL, [SiteID] NCHAR(10) NULL, [PM10] NCHAR(10) NULL, [NVPM10] NCHAR(10) NULL, [VPM10] NCHAR(10) NULL, [NVPM2.5] NCHAR(10) NULL, [PM2.5] NCHAR(10) NULL, [VPM2.5] NCHAR(10) NULL, [CO] NCHAR(10) NULL, [O3] NCHAR(10) NULL,  [SO2] NCHAR(10) NULL, [Temperature] NCHAR(10) NULL, [RH] NCHAR(10) NULL, [Air Pressure] NCHAR(10) NULL, [Location] NCHAR(10) NULL, [geo_point_2d] NCHAR(10) NULL, [DateStart] NCHAR(10) NULL, [DateEnd] NCHAR(10) NULL,  [Current] NCHAR(10) NULL, [Instrument Type] NCHAR(10) NULL)"



# In[2]:


df=pd.read_csv("Clean.csv")
df

sql = """INSERT INTO pollution_db2 (NO) VALUES(?)"""#.format(group.replace('"', '""'))"""
# """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
# ("INSERT INTO songs (name, filehash) VALUES (?, ?)", values)                          #VALUES (%s, %s, %s, %s) """
val = [
 ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'), ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'), ('1'),
  ('2'),
  ('3'),
    ('4'),
    ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'), ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'), ('1'),
  ('2'),
  ('3'),
    ('4'),
    ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'), ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'), ('1'),
  ('2'),
  ('3'),
    ('4'),
    ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'), ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'),
     ('1'),
  ('2'),
  ('3'),
    ('4'), ('1'),
  ('2'),
  ('3'),
    ('4')
]

with open ('insert-100.sql','w') as file:
    file.write(sql)
file.close()    


# In[3]:


df=df.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1)

print(df.columns)
# In[6]:


conn=sqlite3.connect('pollition_db')
df.to_sql("pollution_db2", con=conn, if_exists="append", index=False)
#database will not connect


# In[7]:


#conn = sqlite3.connect('pollution-db2')
c = conn.cursor()




c.execute('CREATE TABLE IF NOT EXISTS pollution_db2 ([DateTime] INT , [NOx] NCHAR(10) NULL, [NO2] NCHAR(10) NULL, [NO] NCHAR(10) NULL, [SiteID] NCHAR(10) NULL, [PM10] NCHAR(10) NULL, [NVPM10] NCHAR(10) NULL, [VPM10] NCHAR(10) NULL, [NVPM2.5] NCHAR(10) NULL, [PM2.5] NCHAR(10) NULL, [VPM2.5] NCHAR(10) NULL, [CO] NCHAR(10) NULL, [O3] NCHAR(10) NULL,  [SO2] NCHAR(10) NULL, [Temperature] NCHAR(10) NULL, [RH] NCHAR(10) NULL, [Air Pressure] NCHAR(10) NULL, [Location] NCHAR(10) NULL, [geo_point_2d] NCHAR(10) NULL, [DateStart] NCHAR(10) NULL, [DateEnd] NCHAR(10) NULL,  [Current] NCHAR(10) NULL, [Instrument Type] NCHAR(10) NULL)')
conn.commit()


# In[9]:





# In[10]:


c.executemany(sql,val)


# In[11]:


result=c.execute("select *from pollution_db2").fetchall()


# In[12]:


for r in result:
    print(r)


# In[20]:



