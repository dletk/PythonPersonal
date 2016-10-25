
def fibonaci(previous1, previous2, limit, listFibo):
    if previous1>limit:
        return listFibo
    else:
        value = previous1+previous2
        listFibo.append(value)
        fibonaci(value,previous1,limit,listFibo)
    return listFibo

if __name__ == '__main__':
    listFibo = []
    listFibo = fibonaci(2,1,4000000,listFibo)
    # 2 is out of the listFibo but it is a even number
    sumResult = 2
    for num in range(len(listFibo)-1):
        if listFibo[num]%2 == 0:
            sumResult += listFibo[num]
    print(sumResult)