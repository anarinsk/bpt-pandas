#%%
import pandas as pd

# %%
df = pd.read_csv('http://bit.ly/kaggletrain', usecols=[2,4,5,11])
pd.get_dummies(df, drop_first=True)

# %% map 

df = pd.DataFrame(
    {
        'gender': ['male', 'female', 'male', 'female'], 
        'color' : ['red', 'green', 'red', 'blue'], 
        'age'   : [25, 40, 10, 30]
    }
)

df['gender leter'] = df.gender.map({'male': 'M', 'female': 'F'})
# %%
df

# %%
