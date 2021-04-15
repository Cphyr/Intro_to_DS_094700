from statistics import mean, median, variance, correlation
import csv


def load_data(path):
    """
    Loads data from given csv
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                # enumerate generates index together with value
                for i, column_name in enumerate(row):
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    # reproducing column name
                    current_column_name = index_to_column_name[i]
                    data[current_column_name].append(float(value))
    return data


def get_sorted_tuple(tup):
    """
    :arg:
        :param tup: contains sortable objects
        :type tup: Tuple()

    :return:
        A new sorted tuple.
    """
    return tuple(sorted(tup))


def abs(x):
    """
    :arg:
        :param x:
        :type x: Number()

    :return:
        absolute value of x
    """
    if(x >= 0):
        return x
    return -x


def compute_correl(data):
    """
    :arg:
        :param data: data
        :type data: Dict(Str(), Iterbale(Number()))

    :return:
        Computes the correlation between every pair of features.
        Appends the pair of features and the correlations to a dictionary when the
        pair are the key and the correlation is the value.

        min_pair_key - The name of the pair with the lowest correlation
        couple_correl_dic[min_pair_key] - The correlation of the weekest_pair
        max_pair_key - The name of the pair with the strongest correlation
        couple_correl_dic[max_pair_key] - The correlation of the strongest_pair
    """
    # Creates a list of all the pairs of features
    keys = list(data.keys())
    couples = [get_sorted_tuple((a, b)) for i, a in enumerate(keys)
               for b in keys[i + 1:]]

    # Creates the dictionary 'couple_correl_dic'
    # Adds the couples of features as keys and their
    # correlation as value
    couple_correl_dic = {}
    for couple in couples:
        first, second = couple
        couple_correl_dic[couple] = correlation(data[first], data[second])

    # Loops through the dictionary 'couple_correl_dic'
    # and finds the pairs with the biggest and smallest correlation
    items = list(couple_correl_dic.items())
    min_pair_key = items[0][0]
    max_pair_key = items[0][0]
    for item in sorted(items):
        if (abs(item[1]) > abs(couple_correl_dic[max_pair_key])):
            max_pair_key = item[0]
        if (abs(item[1]) < abs(couple_correl_dic[min_pair_key])):
            min_pair_key = item[0]

    # Returns the couple of features with the highest correlation and its correlation
    # and the couple of features with the lowest correlation and its correlation
    return min_pair_key, couple_correl_dic[min_pair_key], max_pair_key, couple_correl_dic[max_pair_key]


def run_analysis():
    file_path = './winequality_2.csv'
    data = load_data(file_path)

    # first way of printing. Everything casted to string, and spaces put automatically between passed values.
    print('Number of features:', len(data))
    for feature_name, list_of_values in sorted(data.items()):
        # second way of printing. We print single string after format function.
        # Format function fills {} with values passed as arguments. It has nice applications for better printing,
        # like limiting number of digits for floats or other formatting tools.
        print('"{}". Mean: {:3.2f}, Median: {:3.2f}, Std: {:3.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values)**0.5))

    # here you should compute correlations. Be careful, pair should be sorted before printing
    weakest_pair, low_correlation, strongest_pair, high_correlation = compute_correl(
        data)
    print('The strongest linear relationship is between: "{}","{}". '
          'The value is: {:3.4f}'.format(strongest_pair[0], strongest_pair[1], high_correlation))

    print('The weakest linear relationship is between: "{}","{}". '
          'The value is: {:3.4f}'.format(*weakest_pair, low_correlation))  # * converts list to arguments.
    # Line 53 is equivalent to line 48, this is just other way to use list as arguments


if __name__ == '__main__':
    run_analysis()
