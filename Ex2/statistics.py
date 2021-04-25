def sum(values):
    """
    Inputs -
        values - List() :: Order():
            List of values which can be sumed

    Outputs -
        The sum over all the elements in values
    """
    sum_val = 0
    # Loop over the elements in values
    for val in values:
        sum_val += val  # add the curr elem to the sum
    return sum_val


def mean(values):
    """
    Inputs -
        values - List() :: Order():
            List of values which can be sumed

    Outputs -
        The mean over all the elements in values

    Externall man-made functions -
        sum() - return the sum of the elements in values
    """
    return sum(values) / len(values)


def median(values):
    """
    Inputs -
        values - List() :: Order():
            List of values which can be sumed

    Outputs -
        The median of the elements in values
    """
    length = len(values)
    sort_vals = sorted(values)  # get a new, sorted, list

    if length % 2 == 1:
        return sort_vals[length // 2]
    return (sort_vals[length // 2 - 1] + sort_vals[length // 2]) / 2
