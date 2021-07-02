import sklearn
import pandas as pd


class Data():

    def __init__(self, path):
        self.preprocess(path)

    def preprocess(self, path):
        df = load_data(path, exclude=["fnlwgt"])
        df = remove_str_from_data(df, "?")  # remove rows with '?'
        df = min_max(df, cols=["age", "education-num",
                     "capital-gain", "capital-loss", "hours-per-week"])
        df = pd.get_dummies(data=df, columns=[
                            "workclass", "education", "martial-status", "occupation",
                            "relationship", "race", "native-country", "sex"])
        self.df = df

    def split_to_k_folds(self, k):
        return sklearn.model_selection.KFold(
            n_splits=k, shuffle=True, random_state=10)


def remove_str_from_data(df, x):
    for C in df:
        df = df[df[C].astype(str).str.contains(str(x), regex=False) != True]
    return df


def load_data(path, exclude=[]):
    data = pd.read_csv(path)
    for col in exclude:
        data.pop(col)

    return data


def min_max(df, cols=[]):

    for C in cols:
        column = df[C]
        df[C] = (column - column.min()) / (column.max() - column.min())

    return df

    pass
