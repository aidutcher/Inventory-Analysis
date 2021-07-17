import pandas as pd
import pyodbc
from datetime import date

# Establish trusted connection to SQL server 
server = 'localhost\SQLEXPRESS'
database = 'Inventory Analysis'
username = 'aidut'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=YES')

# Selecting all data from dc1UsageData, representing the data from one distribution center
select = 'SELECT * FROM dbo.dc1UsageData'

df = pd.read_sql(select,cnxn)

#print(df.columns)
#['ITEM', 'PER1', 'PER2', 'PER3', 'PER4', 'PER5', 'PER6', 'PER7', 'PER8',
#      'PER9', 'PER10', 'PER11', 'PER12', 'Vendor', 'Total_Use', 'Unit_Cost',
#     'Avg_Sell', 'Lead_Time', 'Item_Category']

#print(df.head())
#             ITEM  PER1  PER2  PER3  ...  Unit_Cost  Avg_Sell  Lead_Time  Item_Category
# 0  NOH0H6L3ICV1M  37.0  16.0  19.0  ...      74.56  106.6208          1       Plastics
# 1  NKR8HHK6S586P  12.0   2.0   1.0  ...       8.78   12.5554          8          China
# 2  QNB0VMKRJJAN4   9.0  14.0  12.0  ...      11.66   16.6738         26      Equipment
# 3  ILHUXETF2JQIL   9.0  29.0  12.0  ...      30.88   44.1584         24       Utensils
# 4  NOH1YY4UR7GXY  32.0   4.0   2.0  ...      79.36  113.4848          8       Plastics

low_move_items = df[df['Total_Use']<50]
# This will show us any items that average around 1 unit per week or less
# These items will be considered "low-movement" and are candidates for elimination

# print(low_move_items[['ITEM','Total_Use']])

#              ITEM  Total_Use
# 62   WNVN52DJM6MUW      45.0
# 85   EERO8ECEGRWGT      45.0
# 153  DUVDXGTP2OW1C      25.0
# 239  WNVNRBO94P972      45.0
# 264  WXTN4SYXHWFR5      43.0
# 667  NKRS33VSO32OP      43.0
# 783  XSDOBE7UKPU1T      43.0
# 926  DUVHYFC51UA2U      47.0
# 944  WNVFQ5Q9Z4LWH      40.0
# 978  EERG1HWR8KRCF      48.0

# We can modify our SQL string to select only the low movement items
low_select = "SELECT * FROM dbo.dc1UsageData WHERE Total_Use < 50"
sql_low_move = pd.read_sql(low_select,cnxn)
# print(sql_low_move[['ITEM','Total_Use']])
#             ITEM  Total_Use
# 0  WNVN52DJM6MUW       45.0
# 1  EERO8ECEGRWGT       45.0
# 2  DUVDXGTP2OW1C       25.0
# 3  WNVNRBO94P972       45.0
# 4  WXTN4SYXHWFR5       43.0
# 5  NKRS33VSO32OP       43.0
# 6  XSDOBE7UKPU1T       43.0
# 7  DUVHYFC51UA2U       47.0
# 8  WNVFQ5Q9Z4LWH       40.0
# 9  EERG1HWR8KRCF       48.0

# We want to save these items for future consideration
today = date.today()
file_date = today.strftime("%b-%d-%Y")

file_path = r'C:\Users\aidut\Documents\Inventory\target_items-' + file_date + '.csv'
low_move_items.to_csv(file_path)