# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:13:22 2020

@author: Alex
"""


import numpy as np
import pandas as pd
datadenco=pd.read_csv(r'C:\analytics\datasets\denco_org.csv')
datadenco
#%% Who are the most loyal Customers
datadenco.columns
datadenco.groupby('custname').size() #Make customer table
datadenco.groupby('custname').size().sort_values(ascending=False) #Sort Customer Transaction
datadenco['custname'].value_counts().nlargest(5) #Select the Top 5
#%% Which customers contribute the most to their revenue
datadenco.groupby('custname')['revenue'].sum() #Sum the revenue by each customer
datadenco.groupby('custname')['revenue'].sum().sort_values(ascending=False) #Sort revenue by customers in descending Order
#%% What part numbers bring in to significant portion of revenue
datadenco.groupby('partnum')['revenue'].sum() #Sum/ Group the revenue by part no
datadenco.groupby('partnum')['revenue'].sum().sort_values(ascending=False) #Sort the revenue by decreasing order
datadenco.groupby('partnum')['revenue'].sum().nlargest(10) #Sort the revenue by decreasing order
#%% 
datadenco.groupby('partnum')['margin'].sum() #Sum/ Group the revenue by part no
datadenco.groupby('partnum')['margin'].sum().sort_values(ascending=False) #Sort the revenue by decreasing order
datadenco.groupby('partnum')['margin'].sum().nlargest(10) #Top revenue by part nos
#%%
datadenco.groupby('partnum')['margin'].sum().sort_values(ascending=False)
