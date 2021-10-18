# Based on https://gitlab.com/JohnLogic/ct-reconstruction/-/blob/master/utils.py
# from my MSc thesis project

# Based on https://gitlab.com/JohnLogic/heat-pump-first-paper-project/-/blob/master/utils.py
# from first PhD paper "HeatFlex: Machine learning based data-driven flexibility prediction for individual heat pumps"

import hashlib
import os
from datetime import datetime
from pathlib import Path
from typing import Optional, Any

import git


class FileUtils:

    DEFAULT_TEMP_FOLDER = "./tmp"

    @classmethod
    def apth(cls, path_string) -> str:
        path_obj = Path(path_string)
        absolute_path = str(path_obj.resolve())
        return cls.pth(absolute_path)

    @classmethod
    def pth(cls, path_string) -> str:
        return os.path.join(*path_string.split('/'))

    @classmethod
    def create_dir(cls, path_string : str, fail_if_exists : bool = False) -> str:
        path_obj = Path(path_string)
        path_obj.mkdir(parents=True, exist_ok=not fail_if_exists)
        return str(path_obj.resolve())

    @classmethod
    def file_name(cls, path_string : str, with_extension : bool = False) -> str:
        path_obj = Path(path_string)
        return path_obj.stem if not with_extension else path_obj.name

    @classmethod
    def home_dir(cls) -> str:
        return str(Path.home())

    @classmethod
    def project_root_dir(cls) -> str:
        # NOTE: you need to change the definition according to the directory of 'utils.py'
        return str(Path(__file__).parent)

    @classmethod
    def calculate_hash(cls, file_path:str, buffer_size: int = 65536) -> str:
        file_hash = hashlib.sha256()  # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file_path, 'rb') as f:  # Open the file to read it's bytes
            fb = f.read(buffer_size)  # Read from the file. Take in the amount declared above
            while len(fb) > 0:  # While there is still data being read from the file
                file_hash.update(fb)  # Update the hash
                fb = f.read(buffer_size)  # Read the next block from the file

        return file_hash.hexdigest()
        # print(file_hash.hexdigest())  # Get the hexadecimal digest of the hash

class DateUtils:

    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H-%M-%S"
    DATETIME_FORMAT = "{}_{}".format(DATE_FORMAT, TIME_FORMAT)

    @classmethod
    def now(cls):
        now = datetime.now()
        return now

    @classmethod
    def formatted_datetime_now(cls):
        return datetime.now().strftime(cls.DATETIME_FORMAT)

class ListUtils:

    @classmethod
    def natural_sort(cls, list_to_sort: [str]) -> [str]:
        """ Sort the given list of strings in the way that humans expect.
        """
        import copy, re
        copied_list = copy.deepcopy(list_to_sort)
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        copied_list.sort(key=alphanum_key)
        return copied_list

    @classmethod
    # Provides with a subdict, containing the key intersection having different values
    # Useful when inspecting what values were change between same structured diffs
    # Returns NEW (dict2) values
    def delta_dict(cls, dict1: dict, dict2: dict) -> (dict, dict):
        key_intersection = set(dict1.keys()).intersection(set(dict2.keys()))
        delta_dict_old, delta_dict_new = {}, {}
        for key in key_intersection:
            if (dict1[key] != dict2[key]):
                delta_dict_old[key] = dict1[key]
                delta_dict_new[key] = dict2[key]
        return delta_dict_old, delta_dict_new

    @classmethod
    def flatten_list(cls, list_to_flatten: list) -> list:
        return [item for sublist in list_to_flatten for item in sublist]

    def permute_dict(dictionary: dict) -> [dict]:

        # Inner method to avoid exposing the purely output parameter 'output_dictionary_list'
        def _permute_dict(dictionary: dict, output_dictionary_list: [dict] = [{}]) -> [dict]:
            if (len(dictionary) == 0):
                return output_dictionary_list

            dictionary_copy = dictionary.copy()
            sorted_keys = ListUtils.natural_sort(list(dictionary_copy.keys()))
            first_key = sorted_keys[0]
            # rest_keys = sorted_keys[1:]
            first_key_values = dictionary_copy.pop(first_key)

            def add_to_dict(dictionary: dict, value: dict) -> dict:
                idict = dictionary.copy()
                idict.update(value)
                return idict

            for idx, _ in enumerate(output_dictionary_list):
                output_dictionary_list[idx] = \
                    list(
                        map(
                            lambda value_for_key: add_to_dict(output_dictionary_list[idx],
                                                              {first_key: value_for_key}), first_key_values)
                    )

            return _permute_dict(dictionary=dictionary_copy,
                                 output_dictionary_list=ListUtils.flatten_list(output_dictionary_list))

        return _permute_dict(dictionary)

class FunkyUtils:

    @classmethod
    def len_iterable(cls, iterable):
        # Based on: https://stackoverflow.com/questions/31011631/python-2-3-object-of-type-zip-has-no-len
        return sum(1 for _ in iterable)

    @classmethod
    def grab_first(cls, iterable):
        for item in iterable:
            return item

class ArgParams:

    def __init__(self, args):
        self.args = args
        self.params = {}

    def str_arg(self, name, **kwargs):
        return self.dtype_arg(name, str, **kwargs)

    def int_arg(self, name, **kwargs):
        return self.dtype_arg(name, int, **kwargs)

    def float_arg(self, name, **kwargs):
        return self.dtype_arg(name, float, **kwargs)

    def bool_arg(self, name, required = False, default:Optional[bool] = None):
        # return self.dtype_arg(name, bool, **kwargs) # TODO: fix proper, remove code rep
        if (name not in self.args) or self.args[name] is None:
            if required and default is None:
                raise ValueError(f"Key '{name}' is required and not present in args!")
            else:
                # Sets to default value
                self.params[name] = default
        else:
            self.params[name] = True if (self.args[name] in ["true", "True"]) else False
        return self.params[name]

    def dtype_arg(self, name, dtype, required: bool = False, default = None):
        if (name not in self.args) or self.args[name] is None:
            if required and default is None:
                raise ValueError(f"Key '{name}' is required and not present in args!")
            else:
                # Sets to default value
                self.params[name] = default
        else:
            self.params[name] = dtype(self.args[name])
        return self.params[name]

    def custom_arg(self, name, lambda_arg_to_val, required: bool = False):
        self.params[name] = lambda_arg_to_val(self.args[name])
        return self.params[name]

    def get_params(self):
        return self.params

class RepoUtils:

    @classmethod
    def getRepoHash(cls):
        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.object.hexsha
        return sha

class TypeUtils:

    @classmethod
    def check_args_for_existing(cls, arguments: [Any]) -> bool:
        if (None in arguments):
            raise ValueError(f"Missing mandatory arguments: {arguments}")
        return True