from dataset import *
from models import *

from utils import *
from sklearn.metrics import mean_squared_error

if __name__ == '__main__':

    FileUtils.project_root_dir()

    df = pd.read_parquet(f"{os.path.join(FileUtils.project_root_dir(), 'data','REDD-Cleaned-f32','house_1-channel_1_output_data_points.parquet')}")
    df = df.head(100000)
    DATETIME_COL = 'datetime'

    df[DATETIME_COL] = pd.to_datetime(df[DATETIME_COL], unit='ms')
    heady = df.head(10)

    #%%
    min_date = df['datetime'].min()
    max_date = df['datetime'].max()

    #%%


    def test_model(model, dl, scaler: StandardScaler, metric = root_mean_squared_error()):
        # TODO: remember to compare against RAW dl also
        list_test_rmse = []
        for x, y in dl:
            y_hat_proper = scaler.inverse_transform(model(x).detach())
            y_proper = scaler.inverse_transform(y)
            list_test_rmse.append(np.sqrt(mean_squared_error(y_hat_proper, y_proper)))
        return float(np.mean(np.stack(list_test_rmse)))

    horizon = 30
    memory = 60
    batch_size = 128
    hidden_size = 48
    epochs = 2

    dm = DataModule(df,
                    memory=memory,
                    horizon=horizon,
                    batch_size=batch_size,
                    flatten_xs=False,
                    error_bound=None)

    model = BasicLSTM_simple(hidden_size=hidden_size,
                             output_length=horizon)
    train_dataloader = dm.train_dataloader()

    device = torch.device('cuda')
    cpu_device = torch.device('cpu')
    model = model.to(device)
    loss_foo = root_mean_squared_error()
    optimizer = torch.optim.Adam(model.parameters())

    ###
    # Training loop

    before_training = DateUtils.now()
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
        print(f"Loss at epoch={epoch+1}: {float(epoch_loss)}, took: {DateUtils.now() - before_training}")

    model = model.to(cpu_device)
    model.eval()
    test_rmse = test_model(model, dm.test_dataloader(), scaler=dm.scaler)
    print(f"Test RMSE: {test_rmse}")


