import data as dt
import statistics as st
import sys
import matplotlib.pyplot as plt
import operator
import numpy


def WMA(xs, ys, weights):
    new_ys = []
    for i in range(len(weights)):
        new_ys.append(ys[i])

    for i in range(len(weights), len(ys)):
        vals = ys[i::-1][:len(weights)]
        new_ys.append(sum([x*y for x, y in zip(vals, weights)]))

    wma_ys = []
    for i in range(len(ys)):
        vals = ys[i:0:-1]
        rolling_avg = 0
        con = 0.7
        rol = 1
        for j, val in enumerate(vals):
            rolling_avg += val * (rol * con)
            rol -= rol * con
        rolling_avg += ys[i::-1][-1] * rol
        wma_ys.append(rolling_avg)
        print(rolling_avg)

    print(wma_ys)

    return wma_ys


def GetAxis(holiday):
    # expect features: "cnt, is_holiday, t1, season"
    pah = r"F:\\University\\1st Year\\2nd Semeter\094700 Intro to DS\Intro_to_DS_git_laptop\Intro_to_DS_094700\Ex1\london.csv"
    data = dt.load_data(pah, "cnt, is_holiday, t1, season")
    data = dt.filter_by_feature(data, "is_holiday", [holiday])[0]
    data = dt.filter_by_feature(data, "season", [3])[0]
    # x = data["t1"], y = data["cnt"]
    dc = {}
    for key in data["t1"]:
        dc[key] = 0

    for key, val in zip(data["t1"], data["cnt"]):
        dc[key] += val

    xs = list(dc.keys())
    ys = list(dc.values())

    points = list(zip(xs, ys))
    points.sort(key=operator.itemgetter(0))

    xs = [x for x, y in points]
    ys = [y for x, y in points]
    return xs, ys


def Graph(xs, ys, fig_num, name):
    plt.figure(fig_num)
    plt.title(name)
    plt.plot(xs, ys)

# calc the trendline
    z = numpy.polyfit(xs, ys, 1)
    p = numpy.poly1d(z)
    plt.plot(xs, p(xs), "r--")


def main():
    (xs1, ys1) = GetAxis(1)
    Graph(xs1, ys1, 1, "Holiday and Winter")

    # WMA :

    w = [0.7, 0.3][::-1]
    Graph(xs1, WMA(xs1, ys1, w), 2, "Weekday and Winter (WMA)")

    (xs2, ys2) = GetAxis(0)
    Graph(xs2, ys2, 3, "Weekday and Winter")

    plt.show()


if __name__ == '__main__':
    main()
