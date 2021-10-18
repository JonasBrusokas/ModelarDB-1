from typing import Optional

import numpy as np
import pandas as pd

import torch
from torch.utils.data import Dataset, TensorDataset, DataLoader

from sklearn.preprocessing import StandardScaler
from sktime.forecasting.model_selection import temporal_train_test_split

class TSDataset(Dataset):
    '''
    Custom Dataset subclass.
    Serves as input to DataLoader to transform X
      into sequence data using rolling window.
    DataLoader using this dataset will output batches
      of `(batch_size, seq_len, n_features)` shape.
    Suitable as an input to RNNs.
    '''
    def __init__(self,
                 ts_tensor: torch.tensor,
                 memory: int,
                 horizon: int,
                 flatten: bool = False,
                 ):
        self.ts_tensor = ts_tensor
        self.memory_length = memory
        self.horizon_length = horizon
        self.flatten = flatten

    def __len__(self):
        # return self.X.__len__() - (self.seq_len-1)
        return self.ts_tensor.__len__() - self.memory_length - self.horizon_length + 1

    def __getitem__(self, index):
        x_border = index + self.memory_length
        y_border = x_border + self.horizon_length

        x = self.ts_tensor[index: x_border]
        y = self.ts_tensor[x_border: y_border]

        return (x,y) if self.flatten else (x.unsqueeze(1), y)

class DataModule:

    def __init__(self,
                 df: pd.DataFrame,
                 memory: int,
                 horizon: int,
                 batch_size: int,
                 flatten_xs: bool,
                 error_bound: Optional[int],
                 ):
        self.df = df

        if (error_bound is None):
            column = 'value-R'
        else:
            column = f'value-E{error_bound}'

        self.series = self.df[column]
        self.memory = memory
        self.horizon = horizon
        self.batch_size = batch_size
        self.flatten_xs = flatten_xs
        self.scaler = StandardScaler()
        self.setup()

    def _dl(self, array):
        ds = TSDataset(torch.tensor(array).float(),
                       memory=self.memory,
                       horizon=self.horizon,
                       flatten=self.flatten_xs)
        dl = DataLoader(ds,
                        batch_size = self.batch_size,
                        shuffle = False, num_workers = 0)
        return dl

    def setup(self):
        y_train_and_val, y_test = temporal_train_test_split(self.series, test_size=0.1)
        y_train, y_val = temporal_train_test_split(y_train_and_val, test_size=0.1)

        self.y_train, self.y_val, self.y_test = y_train, y_val, y_test
        self.y_train = self.scaler.fit_transform(self.y_train.to_numpy().reshape(-1, 1)).squeeze()
        self.y_val = self.scaler.transform(self.y_val.to_numpy().reshape(-1, 1)).squeeze()
        self.y_test = self.scaler.transform(self.y_test.to_numpy().reshape(-1, 1)).squeeze()

    def train_dataloader(self):
        return self._dl(self.y_train)

    def val_dataloader(self):
        return self._dl(self.y_val)

    def test_dataloader(self):
        return self._dl(self.y_test)

if __name__ == '__main__':

    print(TSDataset.__name__)

    df = pd.read_parquet("/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet")
    dm = DataModule(df, 16, 4, 32, False, None)

    for x, y in dm.train_dataloader():
        x_id, y_id = x, y
        break