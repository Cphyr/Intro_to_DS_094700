import data as DataPy


def sum(values):
    """sums all of the members in 'values' and returns the sum"""
    CurrentSum = 0
    for i in range(len(values)):
        CurrentSum = CurrentSum + values[i]
    return CurrentSum


def mean(values):
    """gets the sum from the function above, calculate the average"""
    return sum(values) / len(values)


def median(values):
    """ sorts the 'values' list and return the median (with the definition of median)"""
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
    """ if """
    values = [
        data[target][i]
        for i in range(len(data[target]))
        if (
            (is_above and data[treatment][i] > threshold)
            or ((not is_above) and data[treatment][i] <= threshold)
        )
    ]
    DataPy.print_details({target: values}, {target}, statistic_functions)