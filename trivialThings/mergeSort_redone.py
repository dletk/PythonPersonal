def mergeSort(anArray):
    if len(anArray) <= 1:
        return anArray
    else:
        left = mergeSort(anArray[:len(anArray) // 2])
        right = mergeSort(anArray[len(anArray) // 2:])
        return merge(left, right)


def merge(left, right):
    pointer_left = 0
    pointer_right = 0
    finalArray = []
    while pointer_left < len(left) and pointer_right < len(right):
        if left[pointer_left] > right[pointer_right]:
            finalArray.append(right[pointer_right])
            pointer_right += 1
        else:
            finalArray.append(left[pointer_left])
            pointer_left += 1
    if pointer_left >= len(left):
        finalArray += right[pointer_right:]
    else:
        finalArray += left[pointer_left:]

    return finalArray


if __name__ == '__main__':
    print(mergeSort([1, 4, 5, 6, 5, 3, 6, 8, 8, 3, 1, 3, 5, 5, 2]))
    print(mergeSort([1, 2, 3]))
    print(mergeSort([8, 2, 7, 3, 6, 4, 5, 1]))
    print(mergeSort([12, 43, 54, 23, 54, 234, 654, 234, 78, 232, 5425, 1, 34, 6, 2, 7]))
    assert ([1, 2, 3, 4, 5] == mergeSort([5, 4, 3, 2, 1]))
    assert [] == mergeSort([])
