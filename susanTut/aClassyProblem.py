numCase = None
numPeop = None


def main():
    takeInput()


def takeInput():
    global numCase, numPeop, mapPeople, listValue, listSort
    # Take the number of cases as input
    numCase = int(input())
    # loop for the number of cases
    for i in range(numCase):
        mapPeople = {}
        listValue = []
        listSort = []

        numPeop = int(input())
        for j in range(numPeop):
            nameAndClass = input()
            name = nameAndClass[:nameAndClass.find(":")]
            theClass = nameAndClass[nameAndClass.find(":") + 2:len(nameAndClass) - 1 - 5]
            mapPeople[name] = theClass
            mapPeople[name] = mapPeople[name].replace("-","")
        listFinal = compareAndSort(numPeop)
        for name in listFinal:
            print(name+"\n")
        print("==============================")

def compareAndSort(numPP):
    global listValue, listSort
    maxLen = 0
    for x in range(numPP):
        listSort.append("")
    listKey = []
    for key in mapPeople.keys():
        listKey.append(key)
        mapPeople[key] = mapPeople[key].replace("lower","3")
        mapPeople[key] = mapPeople[key].replace("middle","2")
        mapPeople[key] = mapPeople[key].replace("upper","1")
        if len(mapPeople[key])>maxLen:
            maxLen = len(mapPeople[key])
    for key in mapPeople.keys():
        if len(mapPeople[key]) < maxLen:
            mapPeople[key] = "2"*(maxLen - len(mapPeople[key]))+mapPeople[key]

        listValue.append(mapPeople[key])

    listKey = sorted(listKey)
    listValue = sorted(listValue)
    runLen = len(listKey)

    for index in range(runLen):
        key = listKey[index]
        index1 = listValue.index(mapPeople[key])
        listSort[index1] = key
        listValue[index1] = ""

    return listSort

main()