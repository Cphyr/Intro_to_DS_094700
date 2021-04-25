import data
from data import Data


class Districts:

    def __init__(self, dt):
        self.data = dt

    def filter_districts(self, letters):
        new_dist = []
        for dist in self.data.get_all_districts():
            if dist[0] in letters:
                new_dist.append(dist)
        self.data.set_districts_data(new_dist)

    def print_details(self, features, stat_funcs):
        """
        Inputs -
        self.data - Dict():
            All the data
            self.data.keys() - Str()
            self.data.values() - Iterable() :: Order()
        fetures - Iterable() :: Str():
            * All the elems in features must be in self.data.keys()
            features to run the stat_funcs on
        stat_funcs (statistic_functions) -
            Iterable() :: Obj-funcs in statistics.py:
            Function to run

        Outputs -
        prints the statistics of each and every feature
        using funcyions in statistics.py.
        """
        for fe in features:
            # feature: func1, func2, func3 ...
            print(
                f"{fe}: {', '.join([str(func(self.data.data[fe])) for func in stat_funcs])}"
            )

    def determine_day_type(self):
        resigned_healed = self.data.data["resigned_healed"]
        new_positives = self.data.data["new_positives"]

        vals = [int((x - y) > 0)
                for x, y in zip(resigned_healed, new_positives)]
        self.data.data["day_type"] = vals

    def get_districts_class(self):
        self.determine_day_type()
        self.data.data = self.data.data.filter_by_feature("day_type", [1])[0]
