#%% 
import pandas as pd 
import numpy as np 


# %%
nrows, ncols = 1000000, 100 
df_A, df_B, df_C, df_D = (pd.DataFrame(np.random.randn(nrows, ncols)) for i in range(4)) 

# %%
%timeit df_A + df_B + df_C + df_D

# %%
%timeit pd.eval('df_A + df_B + df_C + df_D')

# %%
df = pd.read_csv('/home/bpt-pandas/data/hotel_bookings.csv')

# %%
df.query('adults >2 and lead_time < 40')
# %%

fifa_df = pd.read_csv("/home/bpt-pandas/data/fifa-data.csv", usecols=["Name", "Age", "Nationality", 
                                           "Club", "Overall", "Value", "Wage"])

fifa_df
#%%
fifa_df[['Value', 'Wage']] = fifa_df[['Value', 'Wage']] \
                             .apply(lambda s: s.replace('[\€,)]','', regex=True))

fifa_df['Value'] = fifa_df['Value'].replace({'K':'*1e3', 'M':'*1e6'}, regex=True).map(pd.eval).astype(float)
fifa_df['Wage'] = fifa_df['Wage'].replace({'K':'*1e3', 'M':'*1e6'}, regex=True).map(pd.eval).astype(float)


#%%
(
fifa_df.head(100).sample(100).style.format({"Value": "€{:20,.0f}", "Wage": "€{:20,.0f}"}) # Format Value and Wages
                 .bar(subset='Value', color='lightblue') # Barchart on Value cell background
                 .bar(subset='Wage', color='orange') # Barchart on Wage cell background
                 .background_gradient(subset='Overall', cmap='winter_r') # Gradient on player ratings
                 .applymap(lambda x: f"color: {'red' if x >= 30 else 'black'}", subset='Age')
) # Color all over 30 players red
                     
# %%
