# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 06:47:38 2021

@author: aidut
"""

import pandas as pd
import pyodbc
from datetime import date

# Set date for file names
today = date.today()
file_date = today.strftime("%b-%d-%Y")

# Establish SQL Server connection
server = 'localhost\SQLEXPRESS'
database = 'Inventory Analysis'
username = 'aidut'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=YES')

# Export list of items that should be transfered from DC1 to DC2
# Reverse the comparison operators to get transfers from DC2 to DC1

DC1_to_DC2_SQL = "SELECT dc2.ITEM, dc1.Total_Use AS 'DC1 Use', dc2.Total_Use AS 'DC2 Use'\
FROM dc1UsageData dc1 \
JOIN dc2UsageData dc2 \
ON dc1.ITEM = dc2.ITEM \
WHERE dc1.Total_Use < 50 AND dc2.Total_Use > 50"

DC1_to_DC2_df = pd.read_sql(DC1_to_DC2_SQL,cnxn)

DC1_to_DC2_file_path = r'C:\Users\aidut\Documents\Inventory\DC1_to_DC2-' + file_date + '.csv'
DC1_to_DC2_df.to_csv(DC1_to_DC2_file_path)

# Export list of 10 least profitable items

least_profit_SQL = "SELECT TOP 10\
	ITEM, \
	Item_Category, \
	Total_Use, \
	(Total_Use * Unit_Cost) AS 'Total Cost', \
	(Total_Use * Avg_Sell) AS 'Total Revenue', \
	((Total_Use * Avg_Sell) - (Total_Use * Unit_Cost)) AS 'Total Profit' \
FROM dc1UsageData \
ORDER BY 'Total Profit'"

least_profit_df = pd.read_sql(least_profit_SQL,cnxn)
least_profit_file_path = r'C:\Users\aidut\Documents\Inventory\least_profit-' + file_date + '.csv'
least_profit_df.to_csv(least_profit_file_path)