import data as dt
import statistics as st
import sys


def main(argv):

    data = dt.load_data(argv[1], argv[2])
    dc = {
        "spring": ("season", [0]),
        "summer": ("season", [1]),
        "autumn": ("season", [2]),
        "winter": ("season", [3]),
        "holiday": ("is_holiday", [1]),
        "weekend": ("is_weekend", [1]),
    }

    print("Question 1:")

    for mode in ["Summer", "Holiday", "All"]:
        print(f"{mode}:")
        if mode == "All":
            dt.print_details(
                data, ["hum", "t1", "cnt"], [st.sum, st.mean, st.median]
            )
        else:
            val = dc[mode.lower()]
            dt.print_details(
                dt.filter_by_feature(data, val[0], val[1])[0],
                ["hum", "t1", "cnt"],
                [st.sum, st.mean, st.median],
            )

    print("\nQuestion 2:")

    threshold = 13.0

    winter_data, _ = dt.filter_by_feature(
        data, dc["winter"][0], dc["winter"][1])
    holiday_data, weekday_data = dt.filter_by_feature(
        winter_data, dc["holiday"][0], dc["holiday"][1])

    print(f"If t1<={threshold}, then:")
    print("Winter holiday records:")
    st.population_statistics(
        "Winter holiday records",
        holiday_data,
        "t1",
        "cnt",
        threshold,
        False,
        [st.mean, st.median],
    )
    print("Winter weekday records:")
    st.population_statistics(
        "Winter weekday records",
        weekday_data,
        "t1",
        "cnt",
        threshold,
        False,
        [st.mean, st.median],
    )

    print(f"If t1>{threshold}, then:")
    print("Winter holiday records:")
    st.population_statistics(
        "Winter holiday records",
        holiday_data,
        "t1",
        "cnt",
        threshold,
        True,
        [st.mean, st.median],
    )
    print("Winter weekday records:")
    st.population_statistics(
        "Winter weekday records",
        weekday_data,
        "t1",
        "cnt",
        threshold,
        True,
        [st.mean, st.median],
    )


if __name__ == "__main__":
    main(sys.argv)
