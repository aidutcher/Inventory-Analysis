import pandas as pd
import numpy as np
from numpy.random import randn
import random, string
from datetime import date

# Change the number in range() to set the number of rows
row_count = range(1000)

# Generate a three letter code to identify the vendor the item was purchased from
def gen_vend_code():
    vend_list =[]
    for i in range(10):
        y = ''.join(random.choices(string.ascii_uppercase, k=3))
        vend_list.append(y)
    return vend_list

# Generate a 10 character alphanumeric string to serve as a unique item number
def gen_item_num():
    num_list = []
    for i in row_count:
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        num_list.append(x)
    return num_list

# Concatenate the alphanumerics with the vendor codes    
def gen_prod_num():
    prod_list = []
    vend_list = gen_vend_code()
    num_list = gen_item_num()
    for n in num_list:
        p = random.choice(vend_list) + n
        prod_list.append(p)
    return prod_list

# Generate a cost per unit between 0.01 and 99.99 for each item
def gen_unit_cost():
    cost_list = []
    for c in row_count:
        cost = round(random.uniform(0.01, 99.99), 2)
        cost_list.append(cost)
    return cost_list

# Assign a random product category to each item
def gen_item_cat():
    prod_cat = ['Disposables','Utensils','China','Glassware','Plastics','Textiles','Equipment']
    cat_list = []
    for cat in row_count:
        category = random.choice(prod_cat)
        cat_list.append(category)
    return cat_list

# Create the data frame and add additional columns
np.random.seed(101)

headers = ['PER1', 'PER2', 'PER3', 'PER4', 'PER5','PER6',\
               'PER7','PER8','PER9','PER10','PER11','PER12']

df = pd.DataFrame(randn(1000,12), gen_prod_num(), headers).round(decimals=1) * 10 + 10
df.index.name = 'ITEM'
df['12mo Use'] = df.sum(axis=1)
df['Unit Cost'] = gen_unit_cost()
df['Avg Sell'] = df['Unit Cost']*round(random.uniform(1,2),2) # Generate a random average sell price for each item
df['Item Category'] = gen_item_cat()

# Write the dataframe to csv
today = date.today()
file_date = today.strftime("%b-%d-%Y")

file_path = r'C:\Users\aidut\Documents\Inventory\inv_data-' + file_date + '.csv'

df.to_csv(file_path)
