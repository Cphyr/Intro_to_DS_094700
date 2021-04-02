from data import *
from copy import deepcopy
from functools import reduce
import pandas as pd


def sum(values):
    """sums all of the members in 'values' and returns the sum."""
    CurrentSum = 0
    for x in values:
        CurrentSum += x
    return CurrentSum


def mean(values):
    """gets the sum from the function above, calculate the average."""
    return sum(values) / len(values)


def median(values):
    """ sorts the 'values' list and return the median (with the definition of median)."""
    length = len(values)
    values.sort()

    if length % 2 == 1:
        return values[length // 2]
    return (values[length // 2 - 1] + values[length // 2]) / 2


def population_statistics(
    fea_des,
    data,
    treat,
    tar,
    threshold,
    is_above,
    stat_funcs,
):
    """if is_above is true, creates a list of the members in data[tar], such that the matching data[treat]>threshold.
    else, creates a list of the members in data[tar], such that the matching data[treat]<=threshold.
    then, prints the statistics given ('stat_funcs' AKA 'statistic_functions') of the created list, using data.py's 'print_details'
    """

    dc = {
        "spring": ("season", [0]),
        "summer": ("season", [1]),
        "autumn": ("season", [2]),
        "winter": ("season", [3]),
        "holiday": ("is_holiday", [1]),
        "weekend": ("is_weekend", [1]),
        "weekday": ("is_holiday", [0]),
    }

    # d = deepcopy(data)
    # for x in filter(lambda i: i in dc.keys(), fea_des.split(" ")):
    #    d = filter_by_feature(d, x[0], x[1])[0]
    # d := the filtered data

    d = reduce(
        lambda ac, val: filter_by_feature(ac, val[0], val[1])[0],
        [dc[i.lower()] for i in fea_des.split(" ") if i.lower() in dc.keys()],
        data,
    )
    if is_above == False:
        df = pd.DataFrame(data)
        df.to_csv("data2.csv")
        df = pd.DataFrame(d)
        df.to_csv(f"{fea_des}.csv")
    print(len(d["season"]))
    print(len(d["is_holiday"]))

    print(treat, tar)

    print_details(
        {tar: [x for x, y in zip(d[tar], d[treat]) if (is_above ^ (y <= threshold))]},
        [tar],
        stat_funcs,
    )  # it's exactly 115 chars (without tabs of course), hence, it's one line
