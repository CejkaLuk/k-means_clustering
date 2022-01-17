from kmeans import KMeans
from configurationloader import ConfigurationLoader


if __name__ == '__main__':
    config = ConfigurationLoader(config_name='CALIFORNIA').config

    kmeans = KMeans(n_clusters=config["n_clusters"],
                    data_file_path=config["data_file_path"])

    kmeans.run()
