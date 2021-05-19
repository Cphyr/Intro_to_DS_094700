import pandas
import sample


class Data:
    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        """
        Params:
            self: Data object
        """
        genes_keys = filter(lambda x: x not in [
                            "samples", "type"], self.data.keys())  # Only the keys to the genes
        num_of_lines = len(self.data['samples'])

        new_list = []
        for i in range(num_of_lines):  # Loops through every row
            # Puts the genes in the row in a list
            genes = [self.data[key][i] for key in genes_keys]
            # Creates the Sample object and adds it to the list
            new_list.append(
                sample.Sample(self.data["samples"][i], genes, self.data["type"][i]))
        return new_list

    def print_details(self, silhouette):
        samples = self.create_samples()
        dominant_label = max(set(samples), key=samples.count)

        print(
            f"{sorted([x.s_id for x in samples])}, dominant label = {dominant_label}, silhouette = {silhouette}")
