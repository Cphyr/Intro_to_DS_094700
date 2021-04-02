import sys
import pandas
import statistics as st
import data

path = r"G:\\University\\1st Year\\2nd Semeter\\094700 Intro to DS\\Intro_to_DS_094700\\Ex1\\london_sample.csv"
df = pandas.read_csv(path)
data = df.to_dict(orient="list")

statistic_functions = ["sum", "mean"]
print(st.sum({1, 2, 3}))
