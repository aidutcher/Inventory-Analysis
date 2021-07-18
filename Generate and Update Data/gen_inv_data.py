import pandas as pd
import numpy as np
from numpy.random import randn
import random, string
from datetime import date

def gen_vend_code():
    vend_list =[]
    for i in range(10):
        y = ''.join(random.choices(string.ascii_uppercase, k=3))
        vend_list.append(y)
    return vend_list

def gen_item_num():
    num_list = []
    for i in range(1000):
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        num_list.append(x)
    return num_list
    
def gen_prod_num():
    prod_list = []
    vend_list = gen_vend_code()
    num_list = gen_item_num()
    for n in num_list:
        p = random.choice(vend_list) + n
        prod_list.append(p)
    return prod_list

np.random.seed(101)

headers = ['PER1', 'PER2', 'PER3', 'PER4', 'PER5','PER6',\
               'PER7','PER8','PER9','PER10','PER11','PER12']

df = pd.DataFrame(randn(1000,12), gen_prod_num(), headers).round(decimals=1) * 10 + 10
df.index.name = 'ITEM'
df['Vendor'] = df.index.astype(str).str.slice(stop=3)
df['Total Use'] = df.sum(axis=1)
df['Unit Cost'] = gen_unit_cost()
df['Avg Sell'] = df['Unit Cost']*round(random.uniform(1,2),2) # Generate a random average sell price for each item
df['Lead Time'] = gen_lead_time()
df['Item Category'] = gen_item_cat()

today = date.today()
file_date = today.strftime("%b-%d-%Y")

file_path = r'your file path here\inv_data-' + file_date + '.csv'

df.to_csv(file_path)
