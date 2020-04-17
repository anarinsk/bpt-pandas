# %%
import pandas as pd
import os 
from glob import glob
import numpy as np

# %% Reading zpped file 
zipped = 'http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Downloads/Inpatient_Data_2013_CSV.zip'
df = pd.read_csv(zipped)
df

# %% assiging types  
df =  pd.read_csv('http://bit.ly/drinksbycountry')
df = df.dtypes.to_frame().reset_index()
df.columns = ['col_name', 'dtype']
df.set_index(['col_name'], inplace=True)
df_dict = df['dtype'].to_dict()

df = pd.read_csv('http://bit.ly/drinksbycountry', dtype=df_dict)
df.dtypes
df
# %%
