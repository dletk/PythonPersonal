def selectionSort(anArr):
    for index in range(len(anArr)):
        subArra = anArr[index:]
        maxV = subArra[0]
        index_max = 0
        for index_2 in range(len(subArra)):
            if subArra[index_2] > maxV:
                index_max = index_2
                maxV = subArra[index_2]
        temp_ele = anArr[-1]
        anArr[-1] = maxV
        anArr[index+index_max] = temp_ele

    return anArr

if __name__ == '__main__':
    print(selectionSort([8,2,7,3,6,4,5,1]))