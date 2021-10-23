from utils import *

import pandas as pd

forecasting_csv_path_string = f"{os.path.join(FileUtils.project_root_dir(), 'results', 'forecasting_results', 'combined', 'combined_10-19.csv')}"
compression_csv_path_string = f"{os.path.join(FileUtils.project_root_dir(), 'results', 'compression_details', 'output.csv')}"

#%%
# Compression CSV
compression_df = pd.read_csv(compression_csv_path_string)

# Filter out LSTM (as the results are crap)

#%%
# Forecasting CSV

forecasting_df = pd.read_csv(forecasting_csv_path_string)
proper_forecasting_df = forecasting_df[forecasting_df['model_type'] != 'lstm']
proper_forecasting_df = proper_forecasting_df[['dataset_name', 'model_type', 'error_bound', 'train_rmse', 'rmse', 'rmse_on_raw']]

# Renaming dataset_name to 'raw' when the error_bound is -1
proper_forecasting_df.loc[ proper_forecasting_df['error_bound'] == -1, 'dataset_name' ] = 'raw'

# Averaging over RAW cases
proper_forecasting_raw_df = proper_forecasting_df[proper_forecasting_df['dataset_name'] == 'raw']\
    .groupby('model_type').mean()
proper_forecasting_raw_df = proper_forecasting_raw_df.reset_index()
proper_forecasting_raw_df['dataset_name'] = 'raw'
proper_forecasting_raw_df

# Removing the error_bound -1 cases from proper_forecasting_df
proper_forecasting_df = proper_forecasting_df[ proper_forecasting_df['error_bound'] != -1]

# Combining these two datasets into a combined one
combined_forecasting_df = pd.concat([proper_forecasting_df, proper_forecasting_raw_df])

