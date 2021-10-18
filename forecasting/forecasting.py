import pandas as pd

df = pd.read_parquet("/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet")
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


