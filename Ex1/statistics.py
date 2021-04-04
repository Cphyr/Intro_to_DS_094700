from data import *
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
    sort_vals = sorted(values)

    if length % 2 == 1:
        return sort_vals[length // 2]
    return (sort_vals[length // 2 - 1] + sort_vals[length // 2]) / 2


def population_statistics(
    fea_des,
    dt,
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

    # filters the needed features from data (dt)
    for x in filter(lambda i: i.lower() in dc.keys(), fea_des.split(" ")):
        dt = filter_by_feature(dt, dc[x.lower()][0], dc[x.lower()][1])[0]

    # Not allowed, but much prettier code
    # d = reduce(
    #     lambda ac, val: filter_by_feature(ac, val[0], val[1])[0],
    #     [dc[i.lower()] for i in fea_des.split(" ") if i.lower() in dc.keys()],
    #     data,
    # )

    print_details(
        {tar: [x for x, y in zip(dt[tar], dt[treat]) if (
            is_above ^ (y <= threshold))]},
        [tar],
        stat_funcs,
    )  # it's exactly 115 chars (without tabs of course), hence, it's one line
