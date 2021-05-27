class Sample:
    def __init__(self, s_id, genes, label):
        """
        Params:
            self: Sample object
            s_id: int. The id of the sample.
            genes: Iterbale of numbers.
            label: String. The label of the sample
        """
        self.s_id = s_id
        self.genes = genes
        self.label = label

    def compute_euclidean_distance(self, other):
        """
        Params:
            self: Sample object
            other: Sample object
        Returns:
            The euclidean distance as defined.
        """
        return sum([(x-y) ** 2 for x, y in zip(self.genes, other.genes)]) ** 0.5

    def dist(self, other):
        """
        Params:
            self: Sample object
            other: Sample object
        Returns:
            The euclidean distance as defined.
        """
        return self.compute_euclidean_distance(other)
