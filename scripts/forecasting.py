import pandas as pd

df = pd.read_parquet("/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet")

heady = df.head(10)