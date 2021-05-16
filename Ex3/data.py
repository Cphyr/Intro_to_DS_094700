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
        new_dict = self.data.copy()
        num_of_lines = len(my_dict['samples'])  # Creates a new copy self.data
        del new_dict['samples']
        del new_dict['type']  # Only leaves the genes part
        new_list = []
        for i in range(num_of_lines):  # Loops through every row
            # Puts the genes in the row in a list
            genes = [values[i] for values in new_dict.values()]
            # Creates the Sample object and adds it to the list
            new_list.append(
                Sample(self.data["samples"][i], genes, self.data["type"][i]))
        return new_list
