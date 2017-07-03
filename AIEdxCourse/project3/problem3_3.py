import sys
import pandas as pd
import numpy as np
import sklearn.model_selection
import sklearn.svm
import sklearn.tree
import sklearn.ensemble

# Raw input data
input_df = pd.DataFrame([])
features = []
labels = []

# Training and testing data
features_training = []
features_testing = []
labels_training = []
labels_testing = []

# File output
file_out = None


def read_files():
    global input_df, file_out
    name_file_in = sys.argv[1]
    name_file_out = sys.argv[2]
    # Create a pandas dataframe from the csv file
    # This dataframe has 3 columns, A, B, label than can be accessed by input_df["name"]
    input_df = pd.DataFrame.from_csv(name_file_in, index_col=None)
    file_out = open(name_file_out, "w")


def prepare_data():
    global input_df, features, labels, labels_training, labels_testing, features_training, features_testing
    # Get the raw input
    features = np.array(input_df.ix[:, 0:2])
    labels = np.array(input_df["label"])

    # Prepare the training and testing data
    features_training, features_testing, labels_training, labels_testing = sklearn.model_selection.train_test_split(
        features, labels, train_size=0.6, test_size=0.4, stratify=labels)


def testing_linear_kernel():
    global features_training, features_testing, labels_training, labels_testing, file_out
    # Prepare the params and estimator to test for finding the best fit params
    lk_tuned_paras = {"kernel": ["linear"], "C": [0.1, 0.5, 1, 5, 10, 50, 100]}
    svc_estimator = sklearn.svm.SVC()
    # Fit the data and find the best params
    grid_search = sklearn.model_selection.GridSearchCV(svc_estimator, lk_tuned_paras, cv=5)
    grid_search.fit(features_training, labels_training)

    # Get the best fit params
    best_c = grid_search.best_params_["C"]
    best_score = grid_search.best_score_

    model_for_test = sklearn.svm.SVC(C=best_c, kernel="linear")
    # Fit the model by training data
    # model_for_test.fit(features_training, labels_training)
    # Get the score of testing data
    # test_score = model_for_test.score(features_testing, labels_testing)
    test_score = sklearn.metrics.accuracy_score(labels_testing,
                                                sklearn.model_selection.cross_val_predict(model_for_test,
                                                                                          features_testing,
                                                                                          labels_testing, cv=5))
    file_out.write(str("svm_linear") + "," + str(best_score) + "," + str(test_score) + "\n")


def testing_poly_kernel():
    global features_training, features_testing, labels_training, labels_testing, file_out
    # Prepare the params and estimator to test for finding the best fit params
    poly_tuned_paras = {"kernel": ["poly"], "C": [0.1, 1, 3], "degree": [4, 5, 6], "gamma": [0.1, 0.5]}
    svc_estimator = sklearn.svm.SVC()
    # Fit the data and find the best params
    grid_search = sklearn.model_selection.GridSearchCV(svc_estimator, poly_tuned_paras, cv=5)
    grid_search.fit(features_training, labels_training)

    # Get the best fit params
    best_c = grid_search.best_params_["C"]
    best_degree = grid_search.best_params_["degree"]
    best_gamma = grid_search.best_params_["gamma"]
    best_score = grid_search.best_score_

    model_for_test = sklearn.svm.SVC(C=best_c, kernel="poly", gamma=best_gamma, degree=best_degree)
    # Fit the model by training data
    # model_for_test.fit(features_training, labels_training)
    # Get the score of testing data
    test_score = sklearn.metrics.accuracy_score(labels_testing,
                                                sklearn.model_selection.cross_val_predict(model_for_test,
                                                                                          features_testing,
                                                                                          labels_testing,
                                                                                          cv=5))
    file_out.write(str("svm_polynomial") + "," + str(best_score) + "," + str(test_score) + "\n")


def testing_rbf_kernel():
    global features_training, features_testing, labels_training, labels_testing, file_out
    # Prepare the params and estimator to test for finding the best fit params
    rbf_tuned_paras = {"kernel": ["rbf"], "C": [0.1, 0.5, 1, 5, 10, 50, 100], "gamma": [0.1, 0.5, 1, 3, 6, 10]}
    svc_estimator = sklearn.svm.SVC()
    # Fit the data and find the best params
    grid_search = sklearn.model_selection.GridSearchCV(svc_estimator, rbf_tuned_paras, cv=5)
    grid_search.fit(features_training, labels_training)

    # Get the best fit params
    best_c = grid_search.best_params_["C"]
    best_gamma = grid_search.best_params_["gamma"]
    best_score = grid_search.best_score_

    model_for_test = sklearn.svm.SVC(C=best_c, kernel="rbf", gamma=best_gamma)
    # Fit the model by training data
    # model_for_test.fit(features_training, labels_training)
    # Get the score of testing data
    test_score = sklearn.metrics.accuracy_score(labels_testing,
                                                sklearn.model_selection.cross_val_predict(model_for_test,
                                                                                          features_testing,
                                                                                          labels_testing,
                                                                                          cv=5))
    file_out.write(str("svm_rbf") + "," + str(best_score) + "," + str(test_score) + "\n")


def testing_logistic_regression():
    global features_training, features_testing, labels_training, labels_testing, file_out
    # Prepare the params and estimator to test for finding the best fit params
    logRegress_tuned_paras = {"C": [0.1, 0.5, 1, 5, 10, 50, 100]}
    lgR_estimator = sklearn.linear_model.LogisticRegression()
    # Fit the data and find the best params
    grid_search = sklearn.model_selection.GridSearchCV(lgR_estimator, logRegress_tuned_paras, cv=5)
    grid_search.fit(features_training, labels_training)

    # Get the best fit params
    best_c = grid_search.best_params_["C"]
    best_score = grid_search.best_score_

    model_for_test = sklearn.linear_model.LogisticRegression(C=best_c)
    # Fit the model by training data
    # model_for_test.fit(features_training, labels_training)
    # Get the score of testing data
    test_score = sklearn.metrics.accuracy_score(labels_testing,
                                                sklearn.model_selection.cross_val_predict(model_for_test,
                                                                                          features_testing,
                                                                                          labels_testing,
                                                                                          cv=5))
    file_out.write(str("logistic") + "," + str(best_score) + "," + str(test_score) + "\n")


def testing_knn():
    global features_training, features_testing, labels_training, labels_testing, file_out
    # Prepare the params and estimator to test for finding the best fit params
    knn_tuned_paras = {"n_neighbors": range(1, 51), "leaf_size": range(5, 61, 5)}
    knn_estimator = sklearn.neighbors.KNeighborsClassifier()
    # Fit the data and find the best params
    grid_search = sklearn.model_selection.GridSearchCV(knn_estimator, knn_tuned_paras, cv=5)
    grid_search.fit(features_training, labels_training)

    # Get the best fit params
    best_n = grid_search.best_params_["n_neighbors"]
    best_leaf = grid_search.best_params_["leaf_size"]
    best_score = grid_search.best_score_

    model_for_test = sklearn.neighbors.KNeighborsClassifier(n_neighbors=best_n, leaf_size=best_leaf)
    # Fit the model by training data
    # model_for_test.fit(features_training, labels_training)
    # Get the score of testing data
    test_score = sklearn.metrics.accuracy_score(labels_testing,
                                                sklearn.model_selection.cross_val_predict(model_for_test,
                                                                                          features_testing,
                                                                                          labels_testing,
                                                                                          cv=5))
    file_out.write(str("knn") + "," + str(best_score) + "," + str(test_score) + "\n")


def testing_decision_tree():
    global features_training, features_testing, labels_training, labels_testing, file_out
    # Prepare the params and estimator to test for finding the best fit params
    dtree_tuned_paras = {"max_depth": range(1, 51), "min_samples_split": range(2, 11)}
    dtree_estimator = sklearn.tree.DecisionTreeClassifier()
    # Fit the data and find the best params
    grid_search = sklearn.model_selection.GridSearchCV(dtree_estimator, dtree_tuned_paras, cv=5)
    grid_search.fit(features_training, labels_training)

    # Get the best fit params
    best_max_depth = grid_search.best_params_["max_depth"]
    best_min_samples_split = grid_search.best_params_["min_samples_split"]
    best_score = grid_search.best_score_

    model_for_test = sklearn.tree.DecisionTreeClassifier(max_depth=best_max_depth,
                                                         min_samples_split=best_min_samples_split)
    # Fit the model by training data
    # model_for_test.fit(features_training, labels_training)
    # Get the score of testing data
    test_score = sklearn.metrics.accuracy_score(labels_testing,
                                                sklearn.model_selection.cross_val_predict(model_for_test,
                                                                                          features_testing,
                                                                                          labels_testing,
                                                                                          cv=5))
    file_out.write(str("decision_tree") + "," + str(best_score) + "," + str(test_score) + "\n")


def testing_random_forest():
    global features_training, features_testing, labels_training, labels_testing, file_out
    # Prepare the params and estimator to test for finding the best fit params
    rforest_tuned_paras = {"max_depth": range(1, 51), "min_samples_split": range(2, 11)}
    rforest_estimator = sklearn.ensemble.RandomForestClassifier()
    # Fit the data and find the best params
    grid_search = sklearn.model_selection.GridSearchCV(rforest_estimator, rforest_tuned_paras, cv=5)
    grid_search.fit(features_training, labels_training)

    # Get the best fit params
    best_max_depth = grid_search.best_params_["max_depth"]
    best_min_samples_split = grid_search.best_params_["min_samples_split"]
    best_score = grid_search.best_score_

    model_for_test = sklearn.ensemble.RandomForestClassifier(max_depth=best_max_depth,
                                                             min_samples_split=best_min_samples_split)
    # Fit the model by training data
    # model_for_test.fit(features_training, labels_training)
    # Get the score of testing data
    test_score = sklearn.metrics.accuracy_score(labels_testing,
                                                sklearn.model_selection.cross_val_predict(model_for_test,
                                                                                          features_testing,
                                                                                          labels_testing,
                                                                                          cv=5))
    file_out.write(str("random_forest") + "," + str(best_score) + "," + str(test_score) + "\n")


read_files()
prepare_data()
testing_linear_kernel()
testing_poly_kernel()
testing_rbf_kernel()
testing_logistic_regression()
testing_knn()
testing_decision_tree()
testing_random_forest()
