import pandas
import statistics


def load_data(path, features):
    "creates a dictionary 'data' which was returned using pandas' to_dict"
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    return data


def filter_by_feature(data, feature, values):
    """creates two Dictionaries 'data1' 'data2'.
    for every key in data, creates a list as the value of the matching key in data1 and data2.
    for every member in the values of every key in data: if the matching data[feature] is in values, appends him to the value of the key in data1.
    else appends him to the value of the key in data2.
    return data1 and data2
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


def print_details(data, features, statistic_functions):
    """prints the statistics given ('statistic_functions') for every member of given 'features' using statistics.py's functions """
    for fe in features:
        # feature: func1, func2, func3 ...
        print(
            f"{fe}: {', '.join([str(func(data[fe])) for func in statistic_functions])}"
        )
