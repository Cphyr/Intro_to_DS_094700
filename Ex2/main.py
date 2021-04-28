import sys
from data import Data
import districts
from districts import Districts
from statistics import mean, median


def question_1(dis):
    """
    :input:
    :param dis: Obj District()

    :return:
    :filters the districts as required and print the necessary parameters:

    :warning: changes the data in dis
    """
    dis.filter_districts(["S", "L"])
    print("Question 1:")
    dis.print_details(["hospitalized_with_symptoms", "intensive_care",
                      "total_hospitalized", "home_insulation"], [mean, median])


def question_2(dis):
    """
    :input:
    :param dis: Obj District()

    :return:
    :do as required in the pdf:


    """
    # Determine the day types
    dis.determine_day_type()

    # init to zero, a dict that will hold the num of green days
    # in each district
    green_days_dict = {}
    for d in dis.data.get_all_districts():
        green_days_dict[d] = 0

    # go over the data and update @green_days_dict
    for d, green in zip(dis.data.get_all_districts(), dis.data.data["day_type"]):
        # if green == 1: inc
        # else == don't change
        green_days_dict[d] += green
    # result: for each key in green_days_dict, the value is the num of
    # green days recorded in the dataset.

    # finds which dists are bad
    is_distric_bad = list(
        map(lambda x: int((x <= 340)), green_days_dict.values()))

    print("\nQuestion 2:")

    print(f"Number of districts: {len(is_distric_bad)}")
    print(f"Number of not green districts: {sum(is_distric_bad)}")

    is_lockdown = "Yes" if sum(is_distric_bad) > 10 else "No"

    print(f"Will a lockdown be forced on whole of Italy?: {is_lockdown}")


def main(argv):
    # load the data
    data = Data(argv[1])
    # create the districts obj
    dis = Districts(data)

    # Answer q1 with a new district obj cause we'll change the data
    question_1(Districts(Data(argv[1])))

    question_2(dis)


if __name__ == "__main__":
    main(sys.argv)
