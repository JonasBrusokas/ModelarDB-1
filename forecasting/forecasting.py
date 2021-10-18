import datetime

import pandas as pd

from dataset import *
from models import *

if __name__ == '__main__':

    df = pd.read_parquet("/Users/jonasb/repos/ModelarDB-ext/data/REDD-Cleaned-f32/house_1-channel_1_output_data_points.parquet")
    df = df.head(100000)
    DATETIME_COL = 'datetime'

    df[DATETIME_COL] = pd.to_datetime(df[DATETIME_COL], unit='ms')
    heady = df.head(10)

    #%%
    min_date = df['datetime'].min()
    max_date = df['datetime'].max()

    #%%

    def test_model(model, dl, metric = root_mean_squared_error()):
        # TODO: remember to compare against RAW dl also
        list_test_rmse = []
        for x, y in dl:
            list_test_rmse.append(metric(model(x), y))
        return torch.mean(torch.stack(list_test_rmse)).detach().item()

    horizon = 30
    memory = 60
    batch_size = 128
    hidden_size = 48
    epochs = 5

    dm = DataModule(df,
                    memory=memory,
                    horizon=horizon,
                    batch_size=batch_size,
                    flatten_xs=False,
                    error_bound=None)

    model = BasicLSTM_simple(hidden_size=hidden_size,
                             output_length=horizon)
    train_dataloader = dm.train_dataloader()

    device = torch.device('cpu')
    model = model.to(device)
    loss_foo = root_mean_squared_error()
    optimizer = torch.optim.Adam(model.parameters())

    ###
    # Training loop

    before_training = datetime.datetime.now()
    for epoch in range(0, epochs):
        loss_list = []
        for x, y in train_dataloader:
            x = x.to(device)
            y = y.to(device)

            optimizer.zero_grad()

            y_hat = model(x)
            loss = loss_foo(y, y_hat)

            loss_list.append(loss.cpu().detach().numpy())

            loss.backward()
            optimizer.step()

        epoch_loss = np.mean(np.stack(loss_list))
        print(f"Loss at epoch={epoch+1}: {float(epoch_loss)}, took: {datetime.datetime.now() - before_training}")

    print(f"Test results: {test_model(model, dm.test_dataloader())}")


