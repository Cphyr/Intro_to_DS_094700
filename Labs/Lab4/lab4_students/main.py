from sys import argv
import os
from cross_validation import CrossValidation
from knn import KNN
from metrics import accuracy_score
from normalization import *

"""
def load_data_debug():
    input_path = "in1"

    if not os.path.exists(input_path):
        print('Input file does not exist')
        exit(1)

    points = []
    with open(input_path, 'r') as f:
        for index, row in enumerate(f.readlines()):
            row = row.strip()
            values = row.split(',')
            points.append(Point(str(index), values[:-1], values[-1]))
    return points"""


def load_data():
    """
    Loads data from path in first argument
    :return: returns data as list of Point
    """
    if len(argv) < 2:
        print('Not enough arguments provided. Please provide the path to the input file')
        exit(1)
    input_path = argv[1]

    if not os.path.exists(input_path):
        print('Input file does not exist')
        exit(1)

    points = []
    with open(input_path, 'r') as f:
        for index, row in enumerate(f.readlines()):
            row = row.strip()
            values = row.split(',')
            points.append(Point(str(index), values[:-1], values[-1]))
    return points


def run_knn(points):
    """m = KNN(5)
    m.train(points)
    print(f'predicted class: {m.predict(points[0])}')
    print(f'true class: {points[0].label}')
    cv = CrossValidation()
    cv.run_cv(points, 10, m, accuracy_score)"""
    question1(points)  # run question 1
    best_k = question2(points)  # run question 2 and save the best k for q3
    question3(points, best_k)
    question4(points)


def question1(points):
    """"
    Params: 
        points: Iterable of Point objects
    """
    m = KNN(1)
    m.train(points)    # Trains the knn with the points given.
    m.predict(points)  # Tries to predict each of the points
    # print(accuracy_score([p.label for p in points], m.predict(points)))


def question2(points):
    """"
    Params: 
        points: Iterable of Point objects
    Returns:
        best_k: the K to which the accuracy is biggest
    """
    best_k = 0
    best_accuracy = 0
    # Loop over the values of k
    for k in range(1, 30+1):  # range(<inclusive>, <exclusive>)
        m = KNN(k)  # Creates a KNN object
        num_blocks = len(points)
        cv = CrossValidation()
        currentscore = cv.run_cv(
            # Calculates the accuracy of the KNN object with the k given
            points, num_blocks, m, accuracy_score, print_final_score=False)
        if(currentscore > best_accuracy):
            # Checks if the accuracy with the current K is bigger
            # If so, updates the best accuracy and the best K
            best_accuracy = currentscore
            best_k = k
    # print(f"K={best_k}")
    return best_k


def question3(points, best_k):
    """"
    Params: 
        points: Iterable of Point objects
        best_k: the K to which the accuracy is biggest
    """
    print("Question 3:")
    print(f"K={best_k}")
    m = KNN(best_k)  # Create the model
    cv = CrossValidation()
    for n in [2, 10, 20]:  # Iterate over wanted n
        print(f"{n}-fold-cross-validation:")
        # run cross validation of those folds
        cv.run_cv(
            points, n, m, accuracy_score, print_final_score=False, print_fold_score=True)


def question4(points):
    """"
    Params: 
        points: Iterable of Point objects
    """
    print("Question 4:")
    for k in [5, 7]:  # Iterate over wanted k
        print(f"K={k}")
        m = KNN(k)  # Create the model
        cv = CrossValidation()

        # shortcut dicts for printing
        shortcuts_dict = {0: "DummyNormalizer", 1: "SumNormalizer",
                          2: "MinMaxNormalizer", 3: "ZNormalizer"}

        # Iterate over the normalizers
        for i, norm in enumerate([DummyNormalizer(), SumNormalizer(), MinMaxNormalizer(), ZNormalizer()]):
            avg_score = cv.run_cv(norm.transform(
                points), 2, m, accuracy_score, print_final_score=False, print_fold_score=True)

            # Just a fancy printing, to make it look like the wanted output file
            print(
                f"Accuracy of {shortcuts_dict[i]} is {avg_score:.2f}", end='' if k == 7 and i == 3 else '\n\n')


if __name__ == '__main__':
    loaded_points = load_data()
    run_knn(loaded_points)
