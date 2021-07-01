import sklearn
import pandas as pd


class Data():

    def __init__(self, path):
        self.preprocess(path)

    def preprocess(self, path):
        df = load_data(path, ["fnlwgt"])
        df = remove_str_from_data(df, "?")# remove rows with '?'
        
        


    def split_to_k_folds(self, k):
        sklearn.model_selection.KFold(
            n_splits=k, shuffle=True, random_state=10)

def remove_str_from_data(df, x):
    for C in df:
        df = df[df[C].astype(str).str.contains(str(x), regex=False) != True]
    return df

def load_data(path, except=[]):
    data = pd.read_csv(path)
    for col in except:
        data.pop(col)

    return data
