def mergeSort(anArray):
    length = len(anArray)
    if length == 1:
        return anArray
    else:
        left = mergeSort(anArray[:length//2])
        right = mergeSort(anArray[length//2:])
        return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i<len(left):
        result += left[i:]
    else:
        result += right[j:]
    return result


if __name__ == '__main__':
    assert mergeSort([1, 2, 3]) == [1, 2, 3]
    assert mergeSort([1]) == [1]
    assert mergeSort([2,1]) == [1,2]
    assert mergeSort([5,4,3,2,1]) == [1,2,3,4,5]
    assert mergeSort([8,2,5,1,68,82,5,7,23,1,25,6,2,32,12]) == sorted([8,2,5,1,68,82,5,7,23,1,25,6,2,32,12])
    print("All tests passed!")
