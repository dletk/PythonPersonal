from algorithmClass.midTerm.selectionSort import *

def bubbleSort(inputArr):
    lenArr = len(inputArr)

    for index in range(lenArr):
        curr_index = 0
        for index_2 in range(lenArr-index):
            if curr_index<lenArr-1:
                if inputArr[curr_index] > inputArr[curr_index+1]:
                    temp_ele = inputArr[curr_index+1]
                    inputArr[curr_index+1] = inputArr[curr_index]
                    inputArr[curr_index] = temp_ele
            curr_index += 1

    return inputArr

if __name__ == '__main__':
    print(bubbleSort([8,2,7,3,6,4,5,1]))
    print(bubbleSort([12,43,54,23,54,234,654,234,78,232,5425,1,34,6,2,7]))
    print(selectionSort([1,2,3]))
    print(selectionSort([8,2,7,3,6,4,5,1]))