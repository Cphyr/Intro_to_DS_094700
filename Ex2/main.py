import sys
from data import Data
import districts
from districts import Districts
from statistics import mean, median


def question_1(dis):
    dis.filter_districts(["S", "L"])
    print("Question 1:")
    dis.print_details(["hospitalized_with_symptoms", "Intensive_care",
                      "total_hospitalized", "home_insulation"], [mean, median])


def main(argv):
    data = Data(argv[1])
    dis = Districts(data)

    question_1(dis)

    pass


if __name__ == "__main__":
    main(sys.argv)
