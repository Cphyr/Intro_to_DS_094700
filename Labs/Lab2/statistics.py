def median(list_of_values):
    sorted_list = sorted(list_of_values)
    # round to int required because division always produces float
    center_index = int(len(list_of_values)/2)

    # Median value depends on length on list
    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index-1])/2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    return sum(list_of_values)/len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average)**2 for x in list_of_values])
    return squared_sum / (len(list_of_values) - 1)


def standard_deviation(list_of_values):
    """
    :arg:
        :param list_of_values: the first list of data
        :type list_of_values: List()

    :return:
        the standard deviation as defined
    """
    return variance(list_of_values)**0.5


def sub_num_from_iterable(num, iterable):
    """
    :arg:
        :param num: the number to subtract
        :type num: Number()
        :param iterable: an iterable to subtract from
        :type iterable: Iterable()

    :return:
        returns a new list that contains the elements of :iterable:
        each subtracted by :num:
    """
    return list(map(lambda x: x - num, iterable))


def covariance(first_list_of_values, second_list_of_values):
    """
    :arg:
        :param first_list_of_values: the first list of data
        :type first_list_of_values: List()
        :param second_list_of_values: the second list of data
        :type second_list_of_values: List()

    :return:
        the covariance as defined
    """

    # Avrages of the lists
    x_avg = mean(first_list_of_values)
    y_avg = mean(second_list_of_values)

    # Subtract the respective avg from each value in the values
    first_diff_from_avg = sub_num_from_iterable(
        x_avg, first_list_of_values)
    scnd_diff_from_avg = sub_num_from_iterable(
        y_avg, second_list_of_values)

    # Compute the nominator of the covariance as defined
    nominator = sum(
        [x * y for x, y in zip(first_diff_from_avg, scnd_diff_from_avg)]
    )

    # Returns the convariance as defined
    return nominator / (len(first_diff_from_avg) - 1)


def correlation(first_list_of_values, second_list_of_values):
    """
    :arg:
        :param first_list_of_values: the first list of data
        :type first_list_of_values: List()
        :param second_list_of_values: the second list of data
        :type second_list_of_values: List()

    :return:
        the correlation as defined
    """
    # Calls the function standard_deviation
    # to compute the standard deviation
    std_dev1 = standard_deviation(first_list_of_values)
    std_dev2 = standard_deviation(second_list_of_values)

    # Return -2 if correlation is not be defined
    # Makes sure not to divide by 0
    if(std_dev1 == 0 or std_dev2 == 0):
        return -2

    # Computes the correlation as its definition
    denominator = std_dev1 * std_dev2
    cov = covariance(first_list_of_values, second_list_of_values)

    return (cov / denominator)
