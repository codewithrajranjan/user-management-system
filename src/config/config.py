import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(dir_path, "../../resource/config.json")
file_handle = open(json_file_path)
config_data = json.loads(file_handle.read())
file_handle.close()


class ConfigManager:
    @classmethod
    def get_config(cls, key):
        value_from_env = os.getenv(key)
        if value_from_env is not None:
            return value_from_env
        value_from_file = config_data.get(key)
        if value_from_file is not None:
            return value_from_file
        raise KeyError("No config found for the key : {}".format(key))
