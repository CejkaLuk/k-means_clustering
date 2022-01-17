class Cluster:

    def __init__(self, centroid, id: int):
        self.id = id
        self.centroid = centroid
        self.nodes = []
        self.diff_to_last_position = None

    def update_centroid(self):
        """Updates the position of this cluster's centroid based on the mean x and y coordinates of the nodes in this
        cluster."""

        # If this cluster has no nodes, then set the current centroid's position as the new position (to get 0
        # movement distance of the current centroid)
        if len(self.nodes) == 0:
            x_pos = self.centroid.pos.x
            y_pos = self.centroid.pos.y
        else:
            # Calculate the new centroid's position as means of this cluster's node positions
            x_pos = get_mean_of_list([node.pos.x for node in self.nodes])
            y_pos = get_mean_of_list([node.pos.y for node in self.nodes])

        self.centroid.set_position(x_pos, y_pos)

    def plot(self, plt):
        """Plots the nodes of this Cluster."""
        plt.scatter([node.pos.x for node in self.nodes],
                    [node.pos.y for node in self.nodes],
                    label=f'Cluster {self.id}')


def get_mean_of_list(lst) -> float:
    return sum(lst) / len(lst)
