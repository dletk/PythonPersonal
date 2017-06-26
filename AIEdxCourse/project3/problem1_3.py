import csv
import sys
import math


dataInput = []
trueOutput = []
w1 = 1
w2 = 1
# b is the offset, w0, the constant,...
b = 1
weightOutput = []


def read_file():
    nameFileIn = sys.argv[1]
    # Read the training data into a list
    with open(nameFileIn, newline="") as csvFile:
        fileIn = csv.reader(csvFile)
        for line in fileIn:
            dataInput.append(list(map(lambda x: int(x), line)))
    # Get the true label of examples in training data
    for example in dataInput:
        trueOutput.append(example[2])


def perceptron():
    global w1, w2, b
    output = []

    for example in dataInput:
        z = b + w1*example[0] + w2*example[1]
        # This is a sigmoid function to make the value become
        outputLabel = math.tanh(z)
        if outputLabel <= 0:
            output.append(-1)
        else:
            output.append(1)
    return output


def backpropagate(output):
    global w1, w2, b
    # Record the current weights before changing them
    weightOutput.append([w1, w2, b])
    for index in range(len(dataInput)):
        if output[index] != trueOutput[index]:
            w1 += trueOutput[index]*dataInput[index][0]
            w2 += trueOutput[index]*dataInput[index][1]
            b += trueOutput[index]


def learning():
    output = perceptron()
    backpropagate(output)
    while output != trueOutput:
        output = perceptron()
        # Keep changing weights until the model is true with training data
        backpropagate(output)
    write_to_file()
    return output


def write_to_file():
    nameFileOut = sys.argv[2]
    with open(nameFileOut, "w") as fileOut:
        for weights in weightOutput:
            fileOut.write(str(weights[0])+","+str(weights[1])+","+str(weights[2])+"\n")
    fileOut.close()

read_file()
learning()
