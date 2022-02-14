
 # all the packages
import mysql.connector
import csv
import pymysql
import sqlalchemy,pyodbc,os
import pandas as pd

os.getcwd()
os.chdir('D:/onlinework/assignment task/dataset')

print(os.listdir())

import platform

print (platform.node())

import socket
socket.gethostname()

pyodbc.drivers()

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\ProjectsV13;"
    "Database=Database;"
    "Trusted_Connection=yes;")

mysql="CREATE TABLE [table1] ([Date Time] INT NOT NULL PRIMARY KEY, [NOx] NCHAR(10) NULL, [NO2] NCHAR(10) NULL, [NO] NCHAR(10) NULL, [SiteID] NCHAR(10) NULL, [PM10] NCHAR(10) NULL, [NVPM10] NCHAR(10) NULL, [VPM10] NCHAR(10) NULL, [NVPM2.5] NCHAR(10) NULL, [PM2.5] NCHAR(10) NULL, [VPM2.5] NCHAR(10) NULL, [CO] NCHAR(10) NULL, [O3] NCHAR(10) NULL,  [SO2] NCHAR(10) NULL, [Temperature] NCHAR(10) NULL, [RH] NCHAR(10) NULL, [Air Pressure] NCHAR(10) NULL, [Location] NCHAR(10) NULL, [geo_point_2d] NCHAR(10) NULL, [DateStart] NCHAR(10) NULL, [DateEnd] NCHAR(10) NULL,  [Current] NCHAR(10) NULL, [Instrument Type] NCHAR(10) NULL)"

import pandas as pd
# reading the csv file 
df=pd.read_csv("Clean.csv")

df

import sqlite3
import sqlalchemy
# connecting the database
conn=sqlite3.connect('pollition_db')
df.to_sql("pollution_db2", con=conn, if_exists="append", index=False)

#conn = sqlite3.connect('pollution-db2')
c = conn.cursor()

#c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')
#creating the table
c.execute('CREATE TABLE IF NOT EXISTS pollution_db2 ([DateTime] INT NOT NULL PRIMARY KEY, [NOx] NCHAR(10) NULL, [NO2] NCHAR(10) NULL, [NO] NCHAR(10) NULL, [SiteID] NCHAR(10) NULL, [PM10] NCHAR(10) NULL, [NVPM10] NCHAR(10) NULL, [VPM10] NCHAR(10) NULL, [NVPM2.5] NCHAR(10) NULL, [PM2.5] NCHAR(10) NULL, [VPM2.5] NCHAR(10) NULL, [CO] NCHAR(10) NULL, [O3] NCHAR(10) NULL,  [SO2] NCHAR(10) NULL, [Temperature] NCHAR(10) NULL, [RH] NCHAR(10) NULL, [Air Pressure] NCHAR(10) NULL, [Location] NCHAR(10) NULL, [geo_point_2d] NCHAR(10) NULL, [DateStart] NCHAR(10) NULL, [DateEnd] NCHAR(10) NULL,  [Current] NCHAR(10) NULL, [Instrument Type] NCHAR(10) NULL)')
conn.commit()

result=c.execute("select *from pollution_db2").fetchall()
## feteching all the details after converting the sql file in database table

for x in result:
    print(x)