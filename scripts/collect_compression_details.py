import json
from pathlib import Path

import pandas as pd

def flatten(list_to_flatten: list) -> list:
    return [item for sublist in list_to_flatten for item in sublist]

def natural_sort(list_to_sort: [str]) -> [str]:
    """ Sort the given list of strings in the way that humans expect. """
    import copy, re
    copied_list = copy.deepcopy(list_to_sort)
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    copied_list.sort(key=alphanum_key)
    return copied_list

def collect_to_csv(path_json:str):
    json_path_obj = Path(path_json)
    json_path_obj_name_without_suffix = (json_path_obj.name)[:-5]
    print(f"JSON name: '{json_path_obj_name_without_suffix}'")

    with open(path_json, "r") as read_file:
        json_object = json.load(read_file)
        keys = list(json_object.keys())
        value_keys = list(filter(lambda key: key.startswith("value-") and not key.endswith("-R"), keys))
        sorted_value_keys = natural_sort(value_keys)
        # sorted_value_keys = list(map(lambda item: item[len("value-"):], sorted_value_keys))

        result_dict_list = []
        for key in sorted_value_keys:
            result_dict = {}
            selected_error_obj = json_object[key]
            error_bound = int(key[len("value-E"):])
            result_dict['name'] = f"{json_path_obj_name_without_suffix}"
            result_dict['error_bound'] = error_bound
            result_dict['parquet_size_raw'] = selected_error_obj['segments']['parquet']['None']
            result_dict['parquet_size_gzip'] = selected_error_obj['segments']['parquet']['gzip']
            result_dict['mean_absolute_error'] = selected_error_obj['metrics']['Mean_Absolute_Value']
            result_dict['mean_absolute_percentage_error'] = selected_error_obj['metrics']['Mean_Absolute_Percentage_Error']
            result_dict_list.append(result_dict)

        global raw_error_obj
        raw_error_obj = json_object['value-R']
        raw_result_dict = {}
        raw_result_dict['name'] = f"raw"
        raw_result_dict['error_bound'] = 0
        raw_result_dict['parquet_size_raw'] = raw_error_obj['data_points']['parquet']['None']
        raw_result_dict['parquet_size_gzip'] = raw_error_obj['data_points']['parquet']['gzip']
        raw_result_dict['mean_absolute_error'] = 0.0
        raw_result_dict['mean_absolute_percentage_error'] = 0.0

    return json_object, result_dict_list, raw_result_dict

#%%
if __name__ == '__main__':

    import os
    from utils import *
    compression_details_path = f"{os.path.join(FileUtils.project_root_dir(), 'results', 'compression_details')}"
    compression_detail_files = list(filter(lambda file_path: file_path.endswith(".json"), os.listdir(compression_details_path)))

    result_dict_list = []
    for file_path in compression_detail_files:
        absolute_path = os.path.join(compression_details_path, file_path)
        obj, result_dict, raw_result_dict = collect_to_csv(absolute_path)
        result_dict_list.append(result_dict)

    result_dict_list.append([raw_result_dict])

    result_dict_list_flattened = flatten(result_dict_list)
    result_df = pd.DataFrame(result_dict_list_flattened)

    result_df.to_csv(
        os.path.join(compression_details_path, "output.csv"),
        index=False,
    )

    # json_path = "/Users/jonasb/repos/ModelarDB-ext/results/compression_details/lost_gorilla_v1.json"
    # obj, result_dict = collect_to_csv(json_path)

