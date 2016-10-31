def hoarePartition(anArray):
    pivot = anArray[0]
    j = len(anArray)-1
    i = 1

    while j >= i:
        while i <= j and anArray[i] <= pivot:
            i += 1
        while anArray[j] >= pivot and i<=j:
            j -= 1
        if j >= i:
            temp_ele = anArray[i]
            anArray[i] = anArray[j]
            anArray[j] = temp_ele

    temp_ele = anArray[j]
    anArray[j] = anArray[0]
    anArray[0] = temp_ele


    return j


def quickSortHoare(anArray):
    if len(anArray) >= 1:
        s = hoarePartition(anArray)
        left = quickSortHoare(anArray[:s])
        right = quickSortHoare(anArray[s + 1:])
        anArray = left + [anArray[s]] + right
    return anArray


if __name__ == '__main__':
    print(quickSortHoare([3,4]))
    print(quickSortHoare([8, 2, 7, 3, 6, 4, 5, 1]))
    print(quickSortHoare([12, 43, 54, 23, 54, 234, 654, 234, 78, 232, 5425, 1, 34, 6, 2, 7]))
    print(quickSortHoare([10, 9, 8, 7, 6, 5, 4, 4, 3, 2, 1, 0]))
    # print(quickSortHoare([4]))
    # print(quickSortHoare([1, 2]))
    # print(quickSortHoare([2, 1]))
    # print(quickSortHoare([0, 0, 0, 0, 0, 0]))
    # print(hoarePartition([8,2,7,3,6,4,5,1]))
