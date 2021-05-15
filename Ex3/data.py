import pandas


class Data:
    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
