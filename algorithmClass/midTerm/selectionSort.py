from . import bubbleSort

def selectionSort(inArr):

    anArr = inArr
    lenArr = len(anArr)

    for index in range(lenArr):
        maxV = anArr[0]
        index_max = 0
        for index_2 in range(0,lenArr-index):
            if anArr[index_2] > maxV:
                index_max = index_2
                maxV = anArr[index_2]
        temp_ele = anArr[lenArr-index-1]
        anArr[lenArr-index-1] = maxV
        anArr[index_max] = temp_ele

    return anArr


if __name__ == '__main__':
    print(selectionSort([8,2,7,3,6,4,5,1]))
    print(selectionSort([12,43,54,23,54,234,654,234,78,232,5425,1,34,6,2,7]))
    print(bubbleSort([8,2,7,3,6,4,5,1]))
    print(bubbleSort([12,43,54,23,54,234,654,234,78,232,5425,1,34,6,2,7]))