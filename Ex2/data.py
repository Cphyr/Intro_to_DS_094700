import pandas


class Data:

    def __init__(self, path):
        """
        Inputs- 
            self -Data object
            path- String()
                A path to the csv file
        Creates the Data object.
        Creates the property 'data' as a dictionary which is in the path given
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        """
        Inputs- 
            self -Data object :
                All the data
                self.data.keys() - Str()
                self.data.values() - Iterable() :: Order()
        Returns- the value of data["denominazione_region"]
        which is all of the districts
        """
        return self.data["denominazione_region"]

    def set_districts_data(self, districts):
        """
        Inputs- 
            self -Data object :
                All the data
                self.data.keys() - Str()
                self.data.values() - Iterable() :: Order()
        Deletes all of the districts that don't start with a charecter in 'districts'
        """
        self.data = self.filter_by_feature(
            "denominazione_region", districts)[0]

    def filter_by_feature(self, feature, values):
        """
        Inputs -
            self.data - Dict():
                All the data
                self.keys() - Str()
                self.values() - Iterable() :: Order()
            feture - Str():
                * Must be in self.data.keys()
                feature to sort by
            values - Iterable():
                List of values to search for
        Outputs -
            2 dicts 'data1', 'data2'.
            data1 - takes only the samples in <self.data> that the value of the feature
            in the sample is in <values>
            data2 - the complement of data1
        """
        NumberOfLines = len(self.data[feature])  # Num of lines

        # Init dict
        data1 = {}
        data2 = {}
        # add the lists to the dicts
        for key in self.data.keys():
            data1[key] = []
            data2[key] = []

        for i in range(0, NumberOfLines):  # loops through every line.
            if self.data[feature][i] in values:
                for key in self.data.keys():
                    data1[key].append(
                        self.data[key][i]
                    )  # if data[feature] is in values, add it to data1
            else:
                for key in self.data.keys():
                    # else, add it to data 2
                    data2[key].append(self.data[key][i])

        return data1, data2  # returns both of the dicts
