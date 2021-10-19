import pandas as pd

from dataset import *
from models import *

from utils import *
from sklearn.metrics import mean_squared_error

if __name__ == '__main__':

    def test_model(model, dl, scaler: StandardScaler, metric = root_mean_squared_error()):
        list_test_rmse = []
        list_ys = []
        for x, y in dl:
            y_hat_proper = scaler.inverse_transform(model(x).detach())
            y_proper = scaler.inverse_transform(y)
            list_test_rmse.append( np.sqrt(mean_squared_error(y_hat_proper, y_proper))
                                   / len(y_proper) if len(y_proper) != 0 else 1
                                 )
            list_ys.append( (y_proper, y_hat_proper) )
        return float(np.mean(np.stack(list_test_rmse))), list_ys

    def train_model(df: pd.DataFrame,
                    model: nn.Module,
                    memory: int,
                    batch_size: int,
                    error_bound: int,
                    flatten_xs: bool,
                    output_parent_folder: str,
                    output_name: str,
                    ):

        # df = df.head(100000) # TODO: REMOVE!
        dm = DataModule(df,
                        memory=memory,
                        horizon=horizon,
                        batch_size=batch_size,
                        flatten_xs=flatten_xs,
                        error_bound=error_bound)
        raw_dm = DataModule(df,
                        memory=memory,
                        horizon=horizon,
                        batch_size=batch_size,
                        flatten_xs=flatten_xs,
                        error_bound=None)

        train_dataloader = dm.train_dataloader()

        device = torch.device('cuda')
        cpu_device = torch.device('cpu')
        model = model.to(device)
        loss_foo = root_mean_squared_error()
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
        scheduler_lr = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=lr_gamma)

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
            scheduler_lr.step()

            epoch_loss = np.mean(np.stack(loss_list))
            print(f"Loss at epoch={epoch+1}: {float(epoch_loss)}, took: {DateUtils.now() - before_training}")

        model = model.to(cpu_device)
        model.eval()

        test_rmse, raw_test_rmse = -1.0, -1.0
        for y_type in ["raw", "compressed"]:
            if (y_type == "raw"):
                test_rmse, list_ys = test_model(model, dm.test_dataloader(), scaler=dm.scaler)
            else:
                raw_test_rmse, list_ys = test_model(model, raw_dm.test_dataloader(), scaler=dm.scaler)
            total_test_ys = np.concatenate(list(map(lambda array: np.stack(array).reshape(-1, 60), list_ys)), axis=0)
            columns = [f"y_{h_i}" for h_i in range(horizon)] + [f"y_hat_{h_i}" for h_i in range(horizon)]
            ys_df = pd.DataFrame(total_test_ys, columns=columns)
            ys_output_file_path = f"{os.path.join(output_parent_folder, f'{output_name}_y_outputs_{y_type}.csv')}"
            ys_df.to_csv(ys_output_file_path)

        # print(f"Test RMSE: {test_rmse}")
        return model, float(epoch_loss), float(test_rmse), float(raw_test_rmse)

    horizon = 30
    memory = 60
    batch_size = 512
    hidden_size = 16
    epochs = 15
    learning_rate = 0.005
    lr_gamma = 0.9

    before_everything = DateUtils.now()

    output_super_parent_folder = f"{os.path.join(FileUtils.project_root_dir(), 'results', 'forecasting_results', f'{before_everything.month}{before_everything.day}')}"
    output_parent_folder = f"{os.path.join(output_super_parent_folder, f'{before_everything.hour}-{before_everything.minute}')}"
    output_csv_path = f"{os.path.join(output_parent_folder, f'output_{before_everything.month}-{before_everything.day}_{before_everything.hour}-{before_everything.minute}.csv')}"
    FileUtils.create_dir(output_parent_folder)

    # TODO: fill dynamically
    parquet_file_paths = [
        # f"{os.path.join(FileUtils.project_root_dir(), 'data', 'REDD-Cleaned-f32', 'lg_only','house_1-channel_1_output_data_points.parquet')}",
        # f"{os.path.join(FileUtils.project_root_dir(), 'data', 'REDD-Cleaned-f32', 'lg_v3_d5', 'house_1-channel_1_output_data_points.parquet')}",
        # f"{os.path.join(FileUtils.project_root_dir(), 'data', 'REDD-Cleaned-f32', 'lg_v3_d10', 'house_1-channel_1_output_data_points.parquet')}",
        # f"{os.path.join(FileUtils.project_root_dir(), 'data', 'REDD-Cleaned-f32', 'lg_v3_d25', 'house_1-channel_1_output_data_points.parquet')}",
        # f"{os.path.join(FileUtils.project_root_dir(), 'data', 'REDD-Cleaned-f32', 'pmc_only', 'house_1-channel_1_output_data_points.parquet')}",
        f"{os.path.join(FileUtils.project_root_dir(), 'data', 'REDD-Cleaned-f32', 'swing', 'house_1-channel_1_output_data_points.parquet')}",
    ]

    error_bound_list = [0, 1, 2, 5, 10, 25, 50, None]
    model_type_list = ['turbo_lstm']

    hidden_size_list = [hidden_size]
    # hidden_size_list = [4, 8, 16, 32, 48, 80] # TODO: remove for LR

    total_run_count = len(error_bound_list) * len(model_type_list) * len(parquet_file_paths) * len(hidden_size_list)

    current_run = 0
    for parquet_path in parquet_file_paths:
        df = pd.read_parquet(parquet_path)
        for error_bound in error_bound_list:
            for model_type in model_type_list:
                for hidden_size in hidden_size_list:
                    current_run+=1
                    print(f"Current run: {current_run} / {total_run_count} | Date: {DateUtils.now()}")
                    # if (current_run <= 21):
                    #     print("Skipping...")
                    #     continue
                    if (model_type == 'lstm'):
                        model = BasicLSTM_simple(hidden_size=hidden_size,
                                                 output_length=horizon)
                    elif(model_type == 'lr'):
                        model = LinearRegression(memory, horizon)
                    elif(model_type == 'turbo_lstm'):
                        model = LSTM_with_skip(memory_length=memory,
                                               hidden_size=hidden_size,
                                               output_length=horizon)
                    else:
                        raise ValueError(f"Model type: '{model_type}' is unsupported!")

                    flatten_xs = True if model_type in ['lr'] else False

                    dataset_name = str(Path(parquet_path).parent.name)
                    before_training = DateUtils.now()
                    trained_model, train_rmse, rmse, raw_rmse = train_model(
                        df,
                        model=model,
                        memory=memory,
                        batch_size=batch_size,
                        error_bound=error_bound,
                        flatten_xs=flatten_xs,
                        output_parent_folder=output_parent_folder,
                        output_name=f"{model_type}_{dataset_name}_E{error_bound if not None else 'RAW'}"
                    )
                    output_dict = {
                        'dataset_name': dataset_name,
                        'model_type': model_type,
                        'error_bound': error_bound if (error_bound is not None) else -1,
                        'epochs': epochs,
                        'memory': memory,
                        'horizon': horizon,
                        'batch_size': batch_size,
                        'hidden_size': hidden_size if (model_type != 'lr') else -1,
                        'train_rmse': train_rmse,
                        'rmse': rmse,
                        'rmse_on_raw': raw_rmse,
                        'train_start': before_training,
                        'lr': learning_rate,
                        'lr_gamma': lr_gamma,
                    }
                    output_csv_df = None
                    try:
                        output_csv_df = pd.read_csv(output_csv_path)
                        current_output_df = pd.DataFrame(output_dict, index=[1])
                        output_csv_df = pd.concat([output_csv_df, current_output_df])
                        print("Concatenating")
                    except Exception as e:
                        print("Output file does not exist yet!")
                        output_csv_df = pd.DataFrame(output_dict, index=[1])
                    output_csv_df.to_csv(path_or_buf=output_csv_path, index=False, header=True)
                    print(f"Training and inference took: {DateUtils.now() - before_training}")




