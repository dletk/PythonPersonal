def quickSort(anArray):
    length = len(anArray)
    if length <= 1:
        return anArray
    else:
        correct = partition(anArray)
        left = quickSort(anArray[:correct])
        right = quickSort(anArray[correct+1:])
        return left + [anArray[correct]] + right


def partition(anArray):
    nextSwap = 0
    check = 0
    pivot = anArray[0]
    while check < len(anArray):
        if anArray[check] <= pivot:
            temp = anArray[check]
            anArray[check] = anArray[nextSwap]
            anArray[nextSwap] = temp
            nextSwap += 1
        check += 1
    temp = anArray[nextSwap-1]
    anArray[nextSwap-1] = pivot
    anArray[0] = temp
    return nextSwap - 1

if __name__ == '__main__':
    assert quickSort([11]) == [11]
    assert quickSort([1,2,3]) == [1,2,3]
    assert quickSort([5,4,3,2,1]) == [1,2,3,4,5]
    assert quickSort([12, 43, 54, 23, 54, 234, 654, 234, 78, 232, 5425, 1, 34, 6, 2, 7]) == sorted([12, 43, 54, 23, 54, 234, 654, 234, 78, 232, 5425, 1, 34, 6, 2, 7])
    assert quickSort([1,4,5,6,1,4,6,34,6,23,6,723,3]) == sorted([1,4,5,6,1,4,6,34,6,23,6,723,3])
    print("All Tests Passed!!")