anArray = []


def quickSortLomuto(anArray):
    if len(anArray)>=1:
        s = lomutoPartition(anArray)
        left = quickSortLomuto(anArray[:s])
        right = quickSortLomuto(anArray[s+1:])
        anArray = left + [anArray[s]] + right
    return anArray


def lomutoPartition(anArray):
    pivot = anArray[-1]
    index_swap = 0
    for index_loop in range(len(anArray)):
         if anArray[index_loop] < pivot:
            temp_ele = anArray[index_swap]
            anArray[index_swap] = anArray[index_loop]
            anArray[index_loop] = temp_ele
            index_swap += 1
    temp_ele = anArray[index_swap]
    anArray[index_swap] = pivot
    anArray[-1] = temp_ele
    # print(anArray)

    return index_swap


if __name__ == '__main__':
    print(quickSortLomuto([8, 2, 7, 3, 6, 4, 5, 1]))
    print(quickSortLomuto([12, 43, 54, 23, 54, 234, 654, 234, 78, 232, 5425, 1, 34, 6, 2, 7]))
    print(quickSortLomuto([10,9,8,7,6,5,4,4,3,2,1,0]))
    print(quickSortLomuto([4]))
    print(quickSortLomuto([1,2]))
    print(quickSortLomuto([2,1]))
    print(quickSortLomuto([0,0,0,0,0,0]))