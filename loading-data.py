# %%
import pandas as pd
import os 
from glob import glob
import numpy as np

# %% Reading zpped file 
# zipped 
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
# %% Random selction for large dataset 
data_url = 'https://raw.githubusercontent.com/anarinsk/bpt-pandas/master/data/test10t.csv'
df = pd.read_csv(data_url, index_col = 0, skiprows=lambda x: x>0 and np.random.rand() > 0.01)
df

# %% Encoding Korean characters utf-8, cp949, euc-kr 

#%% In non-pandas way 
# from: https://realpython.com/python-matplotlib-guide/

from io import BytesIO
import tarfile
from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz'
b = BytesIO(urlopen(url).read())
fpath = 'CaliforniaHousing/cal_housing.data'

with tarfile.open(mode='r', fileobj=b) as archive:
    housing = np.loadtxt(archive.extractfile(fpath), delimiter=',')

#%%
>>> import matplotlib.pyplot as plt

>>> y = housing[:, -1]
>>> pop, age = housing[:, [4, 7]].T
>>> def add_titlebox(ax, text):
...     ax.text(.55, .8, text,
...         horizontalalignment='center',
...         transform=ax.transAxes,
...         bbox=dict(facecolor='white', alpha=0.6),
...         fontsize=12.5)
...     return ax
>>> gridsize = (3, 2)
>>> fig = plt.figure(figsize=(12, 8))
>>> ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
>>> ax2 = plt.subplot2grid(gridsize, (2, 0))
>>> ax3 = plt.subplot2grid(gridsize, (2, 1))
>>> ax1.set_title('Home value as a function of home age & area population',
...               fontsize=14)
>>> sctr = ax1.scatter(x=age, y=pop, c=y, cmap='RdYlGn')
>>> plt.colorbar(sctr, ax=ax1, format='$%d')
>>> ax1.set_yscale('log')
>>> ax2.hist(age, bins='auto')
>>> ax3.hist(pop, bins='auto', log=True)

>>> add_titlebox(ax2, 'Histogram: home age')
>>> add_titlebox(ax3, 'Histogram: area population (log scl.)')

# %%
