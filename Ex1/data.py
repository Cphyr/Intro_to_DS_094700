import pandas
import statistics


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    return data


def filter_by_feature(data, feature, values):
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
    for func in statistic_functions:
        for feature in features:
            print(
                f"function: {func}, feature: {feature}, output: {getattr(statistics, func)(values=data[feature])}"
            )