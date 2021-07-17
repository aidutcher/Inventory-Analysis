# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 06:42:23 2021

@author: aidut
"""

import pandas as pd
import numpy as np
from datetime import date

df = pd.read_csv(r'C:/Users/aidut/Documents/Inventory/inv_data-Jul-13-2021.csv')

df['12mo Use'] = df.sum(axis=1)

# print(df.head())

#             ITEM  PER1  PER2  PER3  PER4  ...  PER9  PER10  PER11  PER12  12mo Use
# 0  HPD6UT027P136  37.0  16.0  19.0  15.0  ... -10.0   17.0   15.0    4.0     155.0
# 1  THLQ4E2NLGNP8  12.0   2.0   1.0  20.0  ...  13.0   27.0   -7.0   -2.0     161.0
# 2  YZWHZBJNYZO37   9.0  14.0  12.0  12.0  ...   5.0    2.0    1.0   15.0     128.0
# 3  SDNPPD9HYIIYZ   9.0  29.0  12.0  30.0  ...  20.0    8.0   10.0   16.0     155.0
# 4  THLUNBS4I7ANS  32.0   4.0   2.0   7.0  ...   1.0   29.0   -1.0   16.0     142.0

#print(df.describe())

# Lowest 12mo Use is 25, highest is 213

#               PER1         PER2  ...        PER12     12mo Use
# count  1000.000000  1000.000000  ...  1000.000000  1000.000000
# mean     10.247000    10.524000  ...     9.717000   122.097000
# std       9.982166    10.156504  ...    10.327418    33.379931
# min     -21.000000   -24.000000  ...   -24.000000    25.000000
# 25%       3.000000     4.000000  ...     3.000000    98.000000
# 50%      10.000000    10.500000  ...    10.000000   122.000000
# 75%      17.000000    17.000000  ...    17.000000   146.000000
# max      40.000000    50.000000  ...    42.000000   213.000000


# print(df.sort_values(by='12mo Use', axis='index', ascending=True))

#               ITEM  PER1  PER2  PER3  PER4  ...  PER9  PER10  PER11  PER12  12mo Use
# 153  EEFQSI8RTGSRJ  -8.0  15.0  22.0   5.0  ... -11.0   -2.0  -11.0    4.0      25.0
# 944  FSSM18OU90UKK   1.0   2.0  -8.0  13.0  ... -12.0   -5.0    3.0    4.0      40.0
# 264  NTGJTJ5ZLM12O  -8.0   5.0   8.0  16.0  ...  14.0    9.0   -5.0    6.0      43.0
# 783  NTGCE8FHD6K9A -11.0  -3.0   2.0  15.0  ...  10.0    6.0   -2.0    4.0      43.0
# 667  THLUY5JS8D4SJ  -2.0   8.0   0.0  -2.0  ...   6.0    9.0    3.0    7.0      43.0
# ..             ...   ...   ...   ...   ...  ...   ...    ...    ...    ...       ...
# 55   SEHVEHXLEFVI7   9.0  15.0  35.0  20.0  ...  15.0   22.0   21.0    8.0     203.0
# 204  EEFDQQ7T1HNCF  25.0   8.0   9.0   5.0  ...  17.0   14.0   42.0   18.0     204.0
# 790  EEFC6Z1NI6JSC  11.0  15.0   9.0  33.0  ...  17.0   12.0   21.0   15.0     206.0
# 385  SIIPDCK9TFA12  15.0  27.0  11.0  25.0  ...   9.0   20.0   13.0   25.0     208.0
# 574  NTG6CAE26AWTL   7.0  10.0  19.0  11.0  ...  31.0   13.0   23.0   23.0     213.0

target_items = df['12mo Use']<50
# This will show us any items that average around 1 unit per week or less
# These items will be considered "low-movement" and are candidates for elimination

# print(df[target_items])
#               ITEM  PER1  PER2  PER3  PER4  ...  PER9  PER10  PER11  PER12  12mo Use
# 62   SZYAJFXU4TA3G  -3.0   0.0  29.0   1.0  ...   5.0  -15.0   -1.0    2.0      45.0
# 85   SZYKYNJ1LVB3K   3.0   0.0  -2.0   3.0  ...  26.0   18.0   12.0   -6.0      45.0
# 153  EEFQSI8RTGSRJ  -8.0  15.0  22.0   5.0  ... -11.0   -2.0  -11.0    4.0      25.0
# 239  EEF6IOXU6A4O6 -14.0 -12.0   1.0   6.0  ...  -4.0   14.0   12.0    9.0      45.0
# 264  NTGJTJ5ZLM12O  -8.0   5.0   8.0  16.0  ...  14.0    9.0   -5.0    6.0      43.0
# 667  THLUY5JS8D4SJ  -2.0   8.0   0.0  -2.0  ...   6.0    9.0    3.0    7.0      43.0
# 783  NTGCE8FHD6K9A -11.0  -3.0   2.0  15.0  ...  10.0    6.0   -2.0    4.0      43.0
# 926  SDN9SEYZFBI6D  14.0  17.0   3.0   9.0  ...  10.0    2.0   16.0  -12.0      47.0
# 944  FSSM18OU90UKK   1.0   2.0  -8.0  13.0  ... -12.0   -5.0    3.0    4.0      40.0
# 978  SZYJ3S83VHS2M  -5.0  19.0   5.0  15.0  ...   4.0    4.0   12.0    3.0      48.0

# We want to save these items for future consideration
today = date.today()
file_date = today.strftime("%b-%d-%Y")

file_path = r'C:\Users\aidut\Documents\Inventory\target_items-' + file_date + '.csv'
df[target_items].to_csv(file_path)