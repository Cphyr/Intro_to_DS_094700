from data import *


def sum(values):
    """sums all of the members in 'values' and returns the sum."""
    CurrentSum = 0
    for i in range(len(values)):
        CurrentSum = CurrentSum + values[i]
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
    treatment,
    target,
    threshold,
    is_above,
    statistic_functions,
):
    """if is_above is true, creates a list of the members in data[target], such that the matching data[treatment]>threshold.
    else, creates a list of the members in data[target], such that the matching data[treatment]<=threshold.
    then, prints the statistics given ('statistic_functions') of the created list, using data.py's 'print_details'
    """
    print_details(
        {target: list(filter(lambda x: is_above ^ (x <= threshold), data[target]))},
        {target},
        statistic_functions,
    )  # it's exactly 120 chars (without tabs of course)
