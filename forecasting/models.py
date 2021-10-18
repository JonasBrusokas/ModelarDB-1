import torch
import numpy as np
from torch import nn

#%%
# METRICS

# https://discuss.pytorch.org/t/rmse-loss-function/16540/3
class root_mean_squared_error(nn.Module):
    def __init__(self):
        super().__init__()
        self.mse = nn.MSELoss()

    def forward(self, yhat, y):
        return torch.sqrt(self.mse(yhat, y))

class maximum_absolute_error(nn.Module):
    def forward(self, yhat, y):
        return torch.max(torch.abs(torch.sub(y, yhat)))

#%%
# MODELS

class LinearRegression(nn.Module):
    def __init__(self,
                 input_length,
                 output_length,
                 ):
        super(LinearRegression, self).__init__()
        self.input_length = input_length
        self.output_length = output_length
        self.linear = nn.Linear(self.input_length, self.output_length)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred

class BasicLSTM_simple(nn.Module):
    def __init__(self,
                 hidden_size,
                 output_length,
                 num_layers = 1,
                 dropout = 0,
                 n_features = 1,
                 ):
        super(BasicLSTM_simple, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.n_features = n_features
        self.dropout = dropout
        self.output_length = output_length

        self.lstm = nn.LSTM(input_size=n_features,
                            hidden_size=hidden_size,
                            num_layers=num_layers,
                            dropout=dropout,
                            batch_first=True)
        self.linear = nn.Linear(hidden_size, self.output_length)

    def forward(self, x):
        lstm_out, other = self.lstm(x)
        y_pred = self.linear(lstm_out[:, self.output_length])
        return y_pred

if __name__ == '__main__':
    sequence_array = np.array([1,2,3,4,5,6])
    sequence_tensor = torch.from_numpy(sequence_array).unsqueeze(1).unsqueeze(0).float()
    flat_tensor = torch.from_numpy(sequence_array).unsqueeze(0).float()

    model_lr = LinearRegression(6, 1)
    model_lstm = BasicLSTM_simple(16, 1)

    output_lr = model_lr(flat_tensor)
    output_lstm = model_lstm(sequence_tensor)



