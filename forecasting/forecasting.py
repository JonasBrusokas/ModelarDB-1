import datetime

import pandas as pd

from dataset import *
from models import *

df = pd.read_parquet("/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet")
DATETIME_COL = 'datetime'

df[DATETIME_COL] = pd.to_datetime(df[DATETIME_COL], unit='ms')
heady = df.head(10)

#%%
min_date = df['datetime'].min()
max_date = df['datetime'].max()

#%%


horizon = 30
memory = 60
batch_size = 128
hidden_size = 48

dm = DataModule(df,
                memory=memory,
                horizon=horizon,
                batch_size=batch_size,
                flatten_xs=False,
                error_bound=None)

model = BasicLSTM_simple(hidden_size=hidden_size,
                         output_length=horizon)
loss = ...
optimizer = ...

batch = 32
memory = 16
horizon = 2

dm = SineWaveDataModule(
    memory_length=memory,
    batch_size=batch,
    horizon_length=horizon,
    transform_ys=True,
)
dm.setup()
n_features = dm.get_n_features(memory)
train_dataloader = dm.train_dataloader()

device = torch.device('cpu')
lstm_model = BasicLSTM_simple(
    n_features=n_features,
    hidden_size=16,
    num_layers=1,
    dropout=0.1,
    output_length=horizon,
)
lstm_model = lstm_model.to(device)

optimizer = torch.optim.Adam(lstm_model.parameters())
epochs = 10

loss_foo = root_mean_squared_error()

before_training = datetime.datetime.now()
for epoch in range(0, epochs):
    loss_list = []
    for x, y in train_dataloader:
        x = x.to(device)
        y = y.to(device)

        optimizer.zero_grad()

        y_hat = lstm_model(x)
        loss = loss_foo(y, y_hat)

        loss_list.append(loss.cpu().detach().numpy())

        loss.backward()
        optimizer.step()

    epoch_loss = np.mean(np.stack(loss_list))
    print(f"Loss at epoch={epoch+1}: {float(epoch_loss)}, took: {datetime.datetime.now() - before_training}")

def test_model(model, dl, metric = pmetrics.root_mean_squared_error()):
    list_test_rmse = []
    for x, y in dl:
        list_test_rmse.append(metric(model(x), y))
    return torch.mean(torch.stack(list_test_rmse)).detach().item()



