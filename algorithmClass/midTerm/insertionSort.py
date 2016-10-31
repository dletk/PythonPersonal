def insertionSort(inArr):

    lenA = len(inArr)

    for i in range(lenA):
        nextEle = inArr[i]
        if i == 0:
            pass
        else:
            for index in range(i):
                if nextEle <= inArr[index]:
                    inArr = inArr[:i] + inArr[i + 1:]
                    inArr.insert(index,nextEle)
                    break
    return inArr

if __name__ == '__main__':
    print(insertionSort([8, 2, 7, 3, 6, 4, 5, 1]))
    print(insertionSort([12, 43, 54, 23, 54, 234, 654, 234, 78, 232, 5425, 1, 34, 6, 2, 7]))