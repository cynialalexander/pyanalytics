# Linear Regression Assignment
"""
Created on Mon Aug  3 23:31:12 2020

@author: Alex
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model #1st method
import statsmodels.api as sm  #2nd method
import matplotlib.pyplot as plt
import seaborn as sns

url ='https://raw.githubusercontent.com/DUanalytics/datasets/master/R/marketing.csv'
marketing = pd.read_csv(url)
marketing
marketing.data
marketing.head()
marketing.sales.head()
#%% Describe Data
marketing.shape
marketing.ndim
#%%
x = marketing.drop(['sales'],axis=1)
x
y = marketing['sales']
y
type(y)

plt.scatter(x, y)
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
