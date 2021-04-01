from data import *
from copy import deepcopy
from functools import reduce


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
        return values[length / 2]
    return (values[length / 2 - 1] + values[length / 2]) / 2


def population_statistics(
    feature_description,
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
        "spring": ("season", 0),
        "summer": ("season", 1),
        "autumn": ("season", 2),
        "winter": ("season", 3),
        "holiday": ("holiday", 1),
        "weekend": ("weekend", 1),
    }

    # d = deepcopy(data)
    # for x in filter(lambda i: i in dc.keys(), feature_description.split(" ")):
    #    d = filter_by_feature(d, x[0], x[1])[0]

    # d := the filtered data
    d = reduce(
        lambda ac, val: filter_by_feature(ac, val[0], val[1])[0],
        filter(lambda i: i in dc.keys(), feature_description.split(" ")),
        data,
    )

    print_details(
        {tar: [x for x, y in zip(d[tar], d[treat]) if (is_above ^ (y <= threshold))]},
        [tar],
        stat_funcs,
    )  # it's exactly 115 chars (without tabs of course), hence, it's one line
