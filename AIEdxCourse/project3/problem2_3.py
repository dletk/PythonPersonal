import sys
import csv
import pandas as pd

input_data = []
true_label = []
input_dataFrame = None
learning_rate = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 1.1]


def read_files():
    global input_data, input_dataFrame, true_label
    name_file_in = sys.argv[1]
    # Create a data frame contains the training data
    input_dataFrame = pd.read_csv(name_file_in, header=None)
    with open(name_file_in, newline="") as csvFile:
        fileIn = csv.reader(csvFile)
        for lines in fileIn:
            input_data.append(list(map(lambda x: float(x), lines)))
            true_label.append(float(lines[2]))


def scale_data():
    global input_data, input_dataFrame
    # Create a list to remember mean and standard deviation of each feature
    # This list has n-1 element, because there are n-1 features in the data
    list_mean_std = []
    for x in range(len(input_data[0]) - 1):
        # Calculate the mean and stdE of the whole column.
        mean = input_dataFrame[x].mean()
        stdE = input_dataFrame[x].std()
        list_mean_std.append((mean, stdE))
    for example in input_data:
        for feature in range(len(example) - 1):
            example[feature] = (example[feature] - list_mean_std[feature][0]) / list_mean_std[feature][1]


def build_linear_regression():
    num_iterations = 100
    output = []
    for rate in learning_rate:
        b_0 = 0.0
        b_age = 0.0
        b_weight = 0.0
        for i in range(num_iterations):
            fx0 = 0.0
            fx_age = 0.0
            fx_weight = 0.0
            num_samples = len(input_data)
            for index in range(num_samples):
                # Each of the weights correspond to its feature
                fx0 += b_0 + b_age * input_data[index][0] + b_weight * input_data[index][1] - true_label[index]
                fx_age += (b_0 + b_age * input_data[index][0] + b_weight * input_data[index][1] - true_label[index]) \
                          * input_data[index][0]
                fx_weight += (b_0 + b_age * input_data[index][0] + b_weight * input_data[index][1] - true_label[index]) \
                          * input_data[index][1]
            b_0 -= rate*fx0/num_samples
            b_age -= rate*fx_age/num_samples
            b_weight -= rate*fx_weight/num_samples
        output.append((rate, num_iterations, b_0, b_age, b_weight))
    # print(output)
    return output


def write_to_file(output):
    nameFileOut = sys.argv[2]
    with open(nameFileOut, "w") as fileOut:
        for line in output:
            fileOut.write(str(line[0])+","+str(line[1])+","+str(line[2])+","+str(line[3])+","+str(line[4])+"\n")
    fileOut.close()


read_files()
# print(input_data)
scale_data()
# print("========================================")
# print(input_data)
write_to_file(build_linear_regression())
