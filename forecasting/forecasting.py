import pandas as pd

from dataset import *

df = pd.read_parquet("/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet")
DATETIME_COL = 'datetime'

df[DATETIME_COL] = pd.to_datetime(df[DATETIME_COL], unit='ms')
heady = df.head(10)

#%%
min_date = df['datetime'].min()
max_date = df['datetime'].max()

#%%
from sktime.forecasting.model_selection import temporal_train_test_split
y_df = df[f'value-E10']
y_train, y_test = temporal_train_test_split(y_df, test_size=0.1)

y_train_ds = TSDataset(y_train, 8, 4)
y_train_dl = DataLoader(y_train_ds,
                         batch_size = 128,
                         shuffle = False,
                         num_workers = 0)

dm = DataModule(df,
                16,
                4,
                32,
                False,
                None)
for X, y in dm.train_dataloader():
    x_i, y_i = X, y
    break

