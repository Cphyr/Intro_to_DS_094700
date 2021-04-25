import sys
from data import Data
import districts
from districts import Districts
from statistics import mean, median


def question_1(dis):
    dis.filter_districts(["S", "L"])
    print("Question 1:")
    dis.print_details(["hospitalized_with_symptoms", "intensive_care",
                      "total_hospitalized", "home_insulation"], [mean, median])


def question_2(dis):

    dis.determine_day_type()

    green_days_dict = {}
    for d in dis.data.get_all_districts():
        green_days_dict[d] = 0

    for d, green in zip(dis.data.get_all_districts(), dis.data.data["day_type"]):
        green_days_dict[d] += green

    is_distric_bad = list(
        map(lambda x: int((x <= 340)), green_days_dict.values()))

    print("\nQuestion 2:")

    print(f"Number of districts: {len(is_distric_bad)}")
    print(f"Number of not green districts: {sum(is_distric_bad)}")

    is_lockdown = "Yes" if sum(is_distric_bad) > 10 else "No"

    print(f"Will a lockdown be forced on whole of Italy?: {is_lockdown}")

    pass


def main(argv):
    data = Data(argv[1])
    dis = Districts(data)

    question_1(Districts(Data(argv[1])))
    question_2(dis)

    pass


if __name__ == "__main__":
    main(sys.argv)
