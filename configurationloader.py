import configparser
import os
from warnings import warn


def load_config_from_file(file_path, config_name) -> dict:
    """Loads a program configuration."""
    if not os.path.exists(file_path):
        raise AssertionError(f'File "{file_path}" not found!')

    cfg = configparser.ConfigParser()
    cfg.read(file_path)

    try:
        config = {"n_clusters": cfg.getint(config_name, 'NumberOfClusters'),
                  "data_file_path": cfg.get(config_name, 'DatasetFilePath')}
    except:
        warn(f'\nConfig "{config_name}" not found in configuration file!\n')
        print(f' Resorting to "DEFAULT" configuration.\n'
              f' Other configuration names are: "DEFAULT", "CALIFORNIA"')
        config = {"n_clusters": cfg.getint('DEFAULT', 'NumberOfClusters'),
                  "data_file_path": cfg.get('DEFAULT', 'DatasetFilePath')}

    return config


class ConfigurationLoader:

    def __init__(self, file_path=None, config_name=None):
        if file_path is not None:
            self.config = load_config_from_file(file_path, config_name)
        else:
            self.config = load_config_from_file('configuration.ini', config_name)
