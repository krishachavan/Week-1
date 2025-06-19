import pandas as pd # data manipulation
import numpy as np # numerical python - linear algebra

from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('PB_All_2000_2021.csv', sep=';')
print(df.head()) 

df.info()

print(df.shape)

print(df.describe().T)

print(df.isnull().sum())

df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
print(df.head())

df.info()

df = df.sort_values(by=['id', 'date'])
print(df.head())

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
print(df.head())

print(df.columns)

print(pollutants = ['NH4', 'BSK5', 'Suspended', 'O2', 'NO3', 'NO2', 'SO4',
       'PO4', 'CL'])
print(df[pollutants].head())