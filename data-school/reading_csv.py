#%% 
import pandas as pd
import os 
from glob import glob
import numpy as np
# %%
df
df = pd.read_csv('data/test-skip.csv', header=2, skiprows=[3,4])
df
# %%
zipped = 'http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Downloads/Inpatient_Data_2013_CSV.zip'
df = pd.read_csv(zipped)
df
#%%
df = pd.DataFrame()
df.to_csv(zipped)

# %%
stockfiles = sorted(glob('data/stock/*.csv'))

# %%
pd.concat([pd.read_csv(file).assign(filename=) for file in stockfiles], ignore_index=True)
# %%

test='data/test/apple.csv'
test
str.split(test, '/')[2]

# %%
def my_str_split(chr, delim, where):
    return str.split(chr, delim)[where]

# %%
my_str_split(my_str_split(test, "/", 2), ".", 0)

# %%
pd.concat([pd.read_csv(file).assign(filename=my_str_split(my_str_split(file, "/", 2), ".", 0) ) for file in stockfiles], ignore_index=True)

# %%
#pd.util.testing.MakeMixedDataFrame()
#df = pd.DataFrame(np.random.rand(10000, 3), columns=list('abc'))
#df.to_csv("data/test10t.csv")

df = pd.read_csv("data/test10t.csv", index_col = 0, skiprows=lambda x: x>0 and np.random.rand() > 0.01)
df
# %% Read from clipboard 
# Should be same OS
df = pd.read_clipboard() 
df

# %% Read from json 
df =pd.read_json('https://api.github.com/users/justmarkham/repos?per_page=100')
df = df[df.fork==False]
df.shape
cols = ['name', 'stargazers_count', 'forks_count']
df[cols].sort_values('stargazers_count', ascending=False)
# %%

# %% Read html 
apple_stock = pd.read_html('https://finance.yahoo.com/quote/AAPL?-AAPL')
pd.concat([apple_stock[0], apple_stock[1]])

# %% Crawling twitter 

url = 'https://en.wikipedia.org/wiki/twitter'
tables = pd.read_html(url)
match_table = pd.read_html(url, match='Follower')
match_table[0]

# %% Assign and query 
df =  pd.read_csv('http://bit.ly/drinksbycountry')
df = df[['country', 'continent', 'beer_servings']]
df.assign(
    continent = df.continent.str.title(),
    beer_ounces = df.beer_servings * 12, 
    beer_gallons = lambda df: df.beer_ounces / 128
).query('beer_gallons > 30'
).style.set_caption('2010년 1인당 맥주 소비량 (단위: 갤론)')

# %% Make new column by f'string 
df_dict = {
    'state':['ny', 'CA', 'TX', "FI"],
    'country':['USA', 'usa', 'uSA', 'Usa']}

df = pd.DataFrame.from_dict(df_dict)

for col in df.columns: 
    df[f'{col}_fixed'] = df[col].str.upper()

df
# %% indexing 

df = pd.DataFrame(
    {
        'col_1':[1,2,3], 
        'col_2':[4,5,6]
    }, index=list('abc')
)
# %%
df.loc['a', 'col_1']
df.iloc[0,0]
df.loc[df.index[0], df.columns[0]]
df.iloc[df.index.get_loc('a'), 0]
df.iloc[df.index.get_loc('a'), df.columns.get_loc('col_1')]

# %%
df =  pd.read_csv('http://bit.ly/drinksbycountry')
#df = df[['country', 'continent', 'beer_servings']]
#df.columns
df.iloc[15:20,:].loc[:, 'beer_servings':'wine_servings']

# %%
df.loc[:, ::-1]
df.loc[::-1]

# %% type testing 

df = pd.DataFrame(
    {
        'customer': ['A', 'B', 'C', 'D'], 
        'sales': [100, '201.2', 325.2, 42.1]
    }
)

df

# %%
df.dtypes
df.sales.apply(type).value_counts()

# %% Hierachical category 

df = pd.DataFrame(
    {
        'id':[101, 102, 103, 104],
        'quality': ['good', 'very good', 'excellent', 'good']
    }
)

cat_type = pd.CategoricalDtype(['good', 'very good', 'excellent'], ordered=True)
df['quality'] = df['quality'].astype(cat_type)
#%%
df.sort_values('quality')
(df.
    query("quality > 'good'"))
# %%
df =  pd.read_csv('http://bit.ly/drinksbycountry')
df = df.dtypes.to_frame().reset_index()
df.columns = ['col_name', 'dtype']
df.set_index(['col_name'], inplace=True)
df_dict = df['dtype'].to_dict()

df = pd.read_csv('http://bit.ly/drinksbycountry', dtype=df_dict)
df.dtypes
#df.columns
#df.columns
#pd.DataFrame(df.dtypes).to_dict()

# %%
