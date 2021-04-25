import data as dpy
import pandas as pd


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


def population_statistics(
    fea_des,
    dt,
    treat,
    tar,
    threshold,
    is_above,
    stat_funcs,
):
    """
    Inputs -
        fea_des - Str():
            Description of the data needed for the
            calculations of the stat_funcs.
            Usge - to filter data by (feature, values) pairs
        dt - Dict():
            All the data
            dt.keys() - Str()
            dt.values() - List() :: Order()
        treat - Str():
            Specific feture of the data
            * Must be in data.keys()
        tar - Str():
            Specific feture of the data
            * Must be in data.keys()
        threshold - Order():
            A value that will be compered to values in data[treat][i]
            * Must be able to cmp to data[treat][i]
        is_above - Bool():
            If true:
                creates a list of the members in data[tar],
                such that the matching data[treat] > threshold
            else:
                same but, data[treat] <= threshold.
        stat_funcs - List() :: Obj-functions:
            List of functions in statistics.py.

    Outputs -
        None

    Main functionality -
        Print the stat_funcs of the values in data[tar] while taking into
        account the matching value in data[treat].
        using data.print_details()
    """

    # Not allowed, but much prettier code
    # d = reduce(
    #     lambda ac, val: filter_by_feature(ac, val[0], val[1])[0],
    #     [dc[i.lower()] for i in fea_des.split(" ") if i.lower() in dc.keys()],
    #     data,
    # )
    new_target_data = [x for x, y in zip(dt[tar], dt[treat]) if (
        is_above ^ (y <= threshold))]
    dpy.print_details(
        {tar: new_target_data},
        [tar],
        stat_funcs,
    )
