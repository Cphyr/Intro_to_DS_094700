import pandas
import statistics


def load_data(path, features):
    """
    Inputs -
        path :: Str():
            contains the path to the csv file
        fetures :: Str():
            the only fields that should be loaded from the csv

    Outputs -
        returns a dictionary of the dataset
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    return data


def filter_by_feature(data, feature, values):
    """
    Inputs -
        data - Dict():
            All the data
            data.keys() - Str()
            data.values() - Iterable() :: Order()
        feture - Str():
            * Must be in data.keys()
            feature to sort by
        values - Iterable():
            List of values to search for
    Outputs -
        2 dicts 'data1', 'data2'.
        data1 - takes only the samples in <data> that the value of the feature
        in the sample is in <values>
        data2 - the complement of data1
    """
    NumberOfLines = len(data[feature])  # Num of lines

    # Init dict
    data1 = {}
    data2 = {}
    # add the lists to the dicts
    for key in data.keys():
        data1[key] = []
        data2[key] = []

    for i in range(0, NumberOfLines):  # loops through every line.
        if data[feature][i] in values:
            for key in data.keys():
                data1[key].append(
                    data[key][i]
                )  # if data[feature] is in values, add it to data1
        else:
            for key in data.keys():
                data2[key].append(data[key][i])  # else, add it to data 2

    return data1, data2  # returns both of the dicts


def print_details(data, features, stat_funcs):
    """
    Inputs -
        data - Dict():
            All the data
            data.keys() - Str()
            data.values() - Iterable() :: Order()
        fetures - Iterable() :: Str():
            * All the elems in features must be in data.keys()
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
            f"{fe}: {', '.join([str(func(data[fe])) for func in stat_funcs])}"
        )
