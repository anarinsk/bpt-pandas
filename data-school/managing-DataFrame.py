#%% 
import pandas as pd 
import numpy as np 

# %% Create DF by dict 

dict = {
    'col_one':[10, 20, 30], 
    'clo_two':[30, 40, 50]}

pd.DataFrame(dict)

#%% Create DF with RV 

pd.DataFrame(np.random.rand(5,4), columns = list('abcd'))

# %% Create sample DF 
df1 = pd.util.testing.makeDataFrame() # contains random values
print("Contains missing values")
df2 = pd.util.testing.makeMissingDataframe() # contains missing values
print("Contains datetime values")
df3 = pd.util.testing.makeTimeDataFrame() # contains datetime values
print("Contains mixed values")
df4 = pd.util.testing.makeMixedDataFrame(); df4.head() # contains mixed values

#%% Make time DF
num_rows = 366 * 24 
pd.util.testing.makeTimeDataFrame(num_rows, freq='H')

# %% Creating Columns 

