#%% 
import pandas as pd 
import numpy as np 

# %%
df = pd.read_csv('http://bit.ly/drinksbycountry')
df
# %%
drink = 'wine'
df[f'{drink}_servings']

# %%
#df.loc[0:4, 'country':'wine_servings']
df.loc[[0,4], ['country','wine_servings']]

# %%
df = pd.DataFrame(
    {
        'col_1':[1,2,3], 
        'col_2':[3,4,5]
    }, 
    index = list('abc')
)

# %%
df.loc['a', 'col_1']
df.iloc[0,0]
# %%
df.loc['a', df.columns[0]]
df.loc[df.index[0], 'col_1']
# %%
df.iloc[df.index.get_loc('a'), 0]

# %%
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.iloc[15:20,:].loc[:, 'beer_servings':'wine_servings']

# %%
drinks.loc[:, ::-1]
drinks.iloc[::-1, :]

# %%
df = pd.DataFrame(np.random.rand(3, 11), columns = list('ABCDEFGHIJK'))

# %%
pd.concat([df.loc[:, 'A':'C'], df.loc[:, 'F'], df.loc[:, 'J':'K']], axis='columns')
df[list(df.columns[0:3]) + list(df.columns[5]) + list(df.columns[9:11])]
df.iloc[:, np.r_[0:3, 5, 9:11]]
# %%
