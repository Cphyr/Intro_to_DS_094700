from sample import *
from cluster import *
import math


class Link:
    # abstract function.
    def compute(self, cluter, other):
        pass


def pair_2_key(first, second):
    """
    Params:
        first: Sample object
        second: Sample object
    Returns:
        returns string that is uniqe to the clusters and their current state.
    """

    sort_pair = sorted([first, second], key=lambda x: x.c_id)
    new_first = sort_pair[0]
    new_second = sort_pair[1]
    return f"{new_first.c_id} {new_first.length} {new_second.c_id} {new_second.length}"


class SingleLink(Link):
    def __init__(self):
        self.name = "single link"

    def compute(self, cluster, other, dists_dict, clusters_dict):
        """
        Params:
            self- SingleLink object
            cluster - Cluster object
            other - Cluster object
        Returns:
            The shortest distance from a sample in 'cluster' to a sample in 'other'
        """
        key = pair_2_key(cluster, other)
        if key in clusters_dict.keys():
            return clusters_dict[key]

        min = math.inf
        # Loops through every pair of samples (one from each cluster object)
        for my_sample in cluster.samples:
            for other_sample in other.samples:
                current = dists_dict[str(
                    sorted([my_sample.s_id, other_sample.s_id]))]
                # If the current distance is smallest than the min, change the min
                if current < min:
                    min = current
        return min


class CompleteLink(Link):
    def __init__(self):
        self.name = "complete link"

    def compute(self, cluster, other, dists_dict, clusters_dict):
        """
        Params:
            self- CompleteLink object
            cluster - Cluster object
            other - Cluster object
        Returns:
            The biggest distance from a sample in 'cluster' to a sample in 'other'
        """
        max = 0
        # Loops through every pair of samples (one from each cluster object)
        for my_sample in cluster.samples:
            for other_sample in other.samples:
                current = dists_dict[str(
                    sorted([my_sample.s_id, other_sample.s_id]))]
                # If the current distance is smallest than the min, change the min
                if current > max:
                    max = current
        return max
