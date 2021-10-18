import numpy as np

import torch
from torch.utils.data import Dataset, TensorDataset, DataLoader

class TSDataset(Dataset):
    '''
    Custom Dataset subclass.
    Serves as input to DataLoader to transform X
      into sequence data using rolling window.
    DataLoader using this dataset will output batches
      of `(batch_size, seq_len, n_features)` shape.
    Suitable as an input to RNNs.
    '''
    # TODO: remove seq_len
    def __init__(self,
                 ts: np.ndarray,
                 memory: int,
                 horizon: int
                 ):
        # TODO: is the .float necessary here
        self.ts_tensor = torch.tensor(ts).float()
        self.memory_length = memory
        self.horizon_length = horizon

    def __len__(self):
        # return self.X.__len__() - (self.seq_len-1)
        return self.ts_tensor.__len__() - self.memory_length - self.horizon_length + 1

    def __getitem__(self, index):
        # return (self.X[index:index+self.seq_len], self.y[index+self.seq_len-1])
        x_border = index + self.memory_length
        y_border = x_border + self.horizon_length
        return (self.ts_tensor[index: x_border],
                self.ts_tensor[x_border: y_border])

if __name__ == '__main__':
    dataset = TSDataset(np.array(list(range(0, 32))), memory=8, horizon=4)

    for x, y in dataset:
        x_i, y_i = x, y
        break

    print(len(dataset))