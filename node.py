from position import Position
from cluster import Cluster


class Node:

    def __init__(self, x: float, y: float):
        self.pos = Position(x, y)
        self.diff_to_last_pos = float('inf')

    def print(self):
        self.pos.print()

    def set_position(self, x: float, y: float):
        """Sets a new position of the node and saves the distance moved."""
        # Save old position to determine how far a node moved
        old_pos = Position(self.pos.x, self.pos.y)

        # Set new position
        self.pos.x = x
        self.pos.y = y

        # Calculate how far the node moved from its old to its new position
        self.diff_to_last_pos = self.pos.distance_to_pos(old_pos)

    def distance_to_node(self, node) -> float:
        """Calculates distance to other node."""
        try:
            return self.pos.distance_to_pos(node.pos)
        except AttributeError:
            raise AssertionError(f'Input variable must be an instance of {type(self).__name__}')

    def assign_to_cluster_by_nearest_centroid(self, clusters: list):
        """Assigns this node to a cluster with the nearest centroid."""
        if not len(clusters) > 0:
            raise AssertionError("Input list must not be empty!")

        cluster = self.get_cluster_by_nearest_centroid(clusters)
        self.assign_to_cluster(cluster)

    def assign_to_cluster(self, cluster):
        """Assigns this node to a cluster"""
        try:
            cluster.nodes.append(self)
        except AttributeError:
            raise AssertionError("Input variable must be an instance of Cluster!")

    def get_cluster_by_nearest_centroid(self, clusters) -> Cluster:
        """Returns the cluster whose centroid is closest to this node by position"""
        try:
            distances = [self.distance_to_node(cluster.centroid) for cluster in clusters]
        except AttributeError:
            raise AssertionError("Input variable must be a list of Cluster instances")

        return clusters[min_value_index_from_list(distances)[1]]


def min_value_index_from_list(lst) -> tuple[float, int]:
    """Returns the minimum value and its index of a list"""

    if not len(lst) > 0:
        raise AssertionError("Input list must not be empty!")

    # Initialize the 1st value as min
    min_value = lst[0]
    min_index = 0

    # Try to find a smaller value
    for i in range(0, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = i

    return min_value, min_index
