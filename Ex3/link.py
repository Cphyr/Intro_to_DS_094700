from sample import compute_euclidean_distance as dist


class Link:

    def compute(self, cluter, other):
        pass


class SingleLink(Link):

    def compute(self, cluster, other):
        """
        Params:
            self- SingleLink object
            cluster - Cluster object
            other - Cluster object
        Returns:
            The shortest distance from a sample in 'cluster' to a sample in 'other'
        """
        # Determines the disteance between the first points as min
        min = cluster[0].dist(other[0])
        # Loops through every pair of samples (one from each cluster object)
        for my_sample in cluster.samples:
            for other_sample in other.samples:
                current = my_sample.dist(other_sample)
                # If the current distance is smallest than the min, change the min
                if current < min:
                    min = current


class CompleteLink(Link):

    def compute(self, cluster, other):
        """
        Params:
            self- CompleteLink object
            cluster - Cluster object
            other - Cluster object
        Returns:
            The biggest distance from a sample in 'cluster' to a sample in 'other'
        """
        # compute the same as explained in SingleLink.compute() but returns the maximum distance
        # instead of the minimum distance
        return max([x.dist(y) for x in cluster.samples for y in other.samples])
