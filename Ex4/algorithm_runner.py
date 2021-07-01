from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.model_selection import cross_validate

class AlgorithmRunner():

    def __init__(self, str_algo):
        if str_algo == "KNN":
            algorithm = KNeighborsClassifier
        elif str_algo == "NC":
            algorithm = NearestCentroid
        else:
            Exception(f"{str_algo} isn't a valid algorithm")

    def calc_acc(data, preds):
        pass

    def calc_precision(data, preds):
        pass

    def calc_recall(data, preds):
        pass

    def run(self, Data, folds=5):
        precision = calc_precision(data, preds)
        recall = calc_recall(data, preds)
        accuracy = calc_acc(data, preds)

        cv = Data.split_to_k_folds(folds)
