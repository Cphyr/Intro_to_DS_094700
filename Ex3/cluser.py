class Cluster:
    def _init_(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
