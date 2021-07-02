from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.model_selection import cross_validate


class AlgorithmRunner():

    def __init__(self, str_algo):
        if str_algo == "KNN":
            model = KNeighborsClassifier
        elif str_algo == "NC":
            model = NearestCentroid
        else:
            raise ValueError(f"{str_algo} isn't a valid algorithm")

    def calc_acc(data, preds):
        pass

    def calc_precision(data, preds):
        pass

    def calc_recall(data, preds):
        pass

    def run(self, df, folds=5):

        X = df.loc[:, df.columns != 'salary']
        y = df.loc[:, df.columns == 'salary']

        cv = df.split_to_k_folds(folds)
        cv_results = cross_validate(self.model, X, y, scoring=[
                                    "precision", "recall", "accuracy"], cv=cv)
