class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples
        self.length = len(samples)

    def merge(self, other):
        """
        Params:
            self: this Cluster object
            other: another Cluster object
        """
        # Changes the c_id to the minimum between the two c_ids
        self.c_id = min(
            self.c_id, other.c_id)
        self.samples = self.samples + other.samples  # Adds the lists together
        # Sorts the list by the s_id of the Samples
        self.samples.sort(key=lambda sample: sample.s_id)
        self.length += other.length
        del other  # Deletes the other cluster

    def print_details(self, silhouette):
        dominant_label = (max(set(self.samples), key=self.samples.count)).label

        # This would probably solve the problem
        # of 2 labels with the same count
        # it will print the one that comes first in an alphabetical order
        label_list = sorted([s.label for s in self.samples])
        dominant_label = (max(label_list, key=lambda l: label_list.count(l)))
        print(
            f"Cluster {self.c_id}: {sorted([x.s_id for x in self.samples])}, dominant label = {dominant_label}, silhouette = {silhouette:.3f}")
