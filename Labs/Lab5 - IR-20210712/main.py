import file_reader
import rocchio_classifier


def calc_accuracy(test_set, classifier):
    correct = 0.0
    total = len(test_set.keys())
    for key in test_set:
        real = test_set[key][-1]
        predicted = classifier.predict(test_set[key][0:-1])
        if real == predicted:
            correct += 1.0
    return correct/total


if __name__ == '__main__':
    print('Accuracy results:')
    file_name = "./dataset/amazon_cells_labelled_full.txt"
    train_file_name = "./dataset/amazon_cells_labelled_train.txt"
    test_file_name = "./dataset/amazon_cells_labelled_test.txt"
    data = file_reader.FileReader(file_name)
    # boolean
    train_set, _ = data.build_set("boolean", train_file_name)
    test_set, _ = data.build_set("boolean", test_file_name)
    classifier = rocchio_classifier.RocchioClassifier(train_set)
    print("Boolean:", '{:.3f}'.format(calc_accuracy(test_set, classifier)))

    # tf
    train_set, _ = data.build_set("tf", train_file_name)
    test_set, _ = data.build_set("tf", test_file_name)
    classifier = rocchio_classifier.RocchioClassifier(train_set)
    print("tf:", '{:.3f}'.format(calc_accuracy(test_set, classifier)))

    # tfidf
    train_set, _ = data.build_set("tfidf", train_file_name)
    test_set, _ = data.build_set("tfidf", test_file_name)
    classifier = rocchio_classifier.RocchioClassifier(train_set)
    print("tfidf:", '{:.3f}'.format(calc_accuracy(test_set, classifier)))

    # tfidf
    train_set, _ = data.build_set("tfidf", train_file_name)
    test_set, _ = data.build_set("tfidf", test_file_name)
    classifier = rocchio_classifier.RocchioClassifier(train_set, cosine_sim=True)
    print("tfidf with cosine similarity:", '{:.3f}'.format(calc_accuracy(test_set, classifier)))
