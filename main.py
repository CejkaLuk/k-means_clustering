from kmeans import KMeans
from configurationloader import ConfigurationLoader


if __name__ == '__main__':
    config = ConfigurationLoader(file_path='configuration.ini',
                                 config_name='SPOTIFY').config
    kmeans = KMeans(config)
    kmeans.run()
