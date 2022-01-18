from node import Node
from cluster import Cluster
from dataloader import DataLoader
import time
import matplotlib.pyplot as plt
from random import choice, sample


class KMeans:

    def __init__(self, n_clusters: int = 2, n_nodes: int = 1000, data_file_path: str = None):
        self.n_clusters = n_clusters
        self.nodes = []
        self.clusters = []

        # Initialize nodes
        if data_file_path is None or not data_file_path:
            self.init_random_nodes(n_nodes)
        else:
            self.init_nodes_from_file(data_file_path)

        self.init_clusters()

        # Matplotlib plot configuration
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)

    def init_nodes_from_file(self, file_path: str):
        """Initializes nodes from csv file"""
        for point in DataLoader(file_path).data:
            self.nodes.append(Node(point[0], point[1]))

    def init_random_nodes(self, n_nodes=1000):
        """Initializes nodes with random coordinates"""
        # Generate n_nodes random x and y coordinates
        x = [choice(range(n_nodes)) for i in range(n_nodes)]
        y = [choice(range(n_nodes)) for i in range(n_nodes)]

        # For each x and y tuple create a new Node
        for coordinates in list(zip(x, y)):
            self.nodes.append(Node(coordinates[0], coordinates[1]))

    def get_random_nodes(self, n_nodes) -> list[Node]:
        """Returns n_nodes random nodes from existing nodes"""
        return [node for node in sample(self.nodes, n_nodes)]

    def init_clusters(self):
        """Initializes num_centroids random nodes as centroids of clusters"""
        centroids = self.get_random_nodes(self.n_clusters)

        # From the list of random nodes (initial centroids) create Clusters - each having a centroid and an id
        for i in range(0, self.n_clusters):
            self.clusters.append(Cluster(centroids[i], i))

    def update_clusters(self):
        """Assigns nodes to clusters with the nearest centroids and updates the centroids."""
        # Reset node assignment to current clusters
        for cluster in self.clusters:
            cluster.nodes = []

        # Assign nodes to clusters - minimum distance to that cluster's centroid
        for node in self.nodes:
            node.assign_to_cluster_by_nearest_centroid(self.clusters)

        # Update centroids of each cluster
        for cluster in self.clusters:
            cluster.update_centroid()

    def run(self):
        """Runs the K-Means procedure"""
        # Initial plot
        self.plot_nodes()
        self.plot_centroids()

        # Update assignment of nodes to clusters
        self.update_clusters()

        # Shrink current graph axis by 20%
        box = self.ax.get_position()
        self.ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

        # Perform K-Means
        while sum([cluster.centroid.diff_to_last_pos for cluster in self.clusters]) > 0:
            # Clear plot
            self.ax.clear()

            # Update assignment of nodes to clusters
            self.update_clusters()

            # Plotting in iteration
            self.plot_clusters()
            self.plot_centroids()

            # Put a legend to the right of the current axis
            self.ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

            # Plot new data
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

            time.sleep(0.5)
            total_centroid_movement = sum([cluster.centroid.diff_to_last_pos for cluster in self.clusters])
            print(f'Total movement of all centroids from last iteration [units]: {total_centroid_movement}')

        input("Press enter to continue...")

    def plot_nodes(self):
        """Plots all existing nodes."""
        self.ax.scatter([node.pos.x for node in self.nodes],
                        [node.pos.y for node in self.nodes])

    def plot_centroids(self):
        """Plots all existing centroids."""
        self.ax.scatter([clstr.centroid.pos.x for clstr in self.clusters],
                        [clstr.centroid.pos.y for clstr in self.clusters],
                        label="Centroids")

    def plot_clusters(self):
        """Plots all existing clusters."""
        for clstr in self.clusters:
            clstr.plot(self.ax)
