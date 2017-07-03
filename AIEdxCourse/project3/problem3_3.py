import sys
import csv
import pandas as pd
import numpy as np
import sklearn.model_selection
import sklearn.svm

# Raw input data
input_df = pd.DataFrame([])
features = []
labels = []

# Training and testing data
features_training = []
features_testing = []
labels_training = []
labels_testing = []

def read_files():
    global input_df
    name_file_in = sys.argv[1]
    # Create a pandas dataframe from the csv file
    # This dataframe has 3 columns, A, B, label than can be accessed by input_df["name"]
    input_df = pd.DataFrame.from_csv(name_file_in, index_col=None)


def prepare_data():
    global input_df, features, labels, labels_training, labels_testing, features_training, features_testing
    # Get the raw input
    features = np.array(input_df.ix[:, 0:2])
    labels = np.array(input_df["label"])

    # Prepare the training and testing data
    features_training, features_testing, labels_training, labels_testing \
        = sklearn.model_selection.train_test_split(features, labels, train_size=0.6, test_size=0.4, stratify=labels)


def testing():
    global features_training, features_testing,labels_training, labels_testing
    lk_tuned_paras = []

read_files()
prepare_data()
print(features_training)
print(labels_training)
