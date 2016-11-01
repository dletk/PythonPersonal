def mergeSort(anArray):

    if len(anArray)>0:
        half = len(anArray)//2

        left = mergeSort(anArray[:half])
        right = mergeSort(anArray[half:])

        result = merge(left, right, anArray)

        return result

    return anArray

def merge(left, right, anArray):
    size_l = len(left)
    size_r = len(right)
    index_right = 0
    index_left = 0
    index_arr = 0
    while index_left < size_l and index_right < size_r:
        if left[index_left] <= right[index_right]:
            anArray[index_arr] = left[index_left]
            index_left += 1
        else:
            anArray[index_arr] = right[index_right]
            index_right += 1
        index_arr += 1
    if index_right == size_r:
        while index_left < size_l:
            anArray[index_arr] = left[index_left]
            index_arr += 1
            index_left += 1
    else:
        while index_right < size_r:
            anArray[index_arr] = right[index_right]
            index_arr += 1
            index_right += 1

    return anArray


if __name__ == '__main__':
    print(mergeSort([8, 2, 7, 3, 6, 4, 5, 1]))
    print(mergeSort([12, 43, 54, 23, 54, 234, 654, 234, 78, 232, 5425, 1, 34, 6, 2, 7]))
