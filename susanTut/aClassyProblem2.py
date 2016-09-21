numCase = None
numPeop = None


def main():
    takeInput()


def takeInput():
    global numCase, numPeop, mapPeople, listValue, listSort
    numRun = 0
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
            if theClass.count("-") <= numRun:
                pass
            else:
                numRun = theClass.count("-")
            mapPeople[name] = theClass[::-1]
            mapPeople[name] = mapPeople[name].replace("-", "")



def compareAndSort(numPP):
    global listValue, listSort
    maxLen = 0
    listSort = []
    listkey = []
    for x in range(numPP):
        listSort.append("")
    for key in mapPeople.keys():
        listkey.append(key)
        mapPeople[key] = mapPeople[key].replace("rewol", "1")
        mapPeople[key] = mapPeople[key].replace("elddim", "2")
        mapPeople[key] = mapPeople[key].replace("reppu", "3")
        if len(mapPeople[key]) > maxLen:
            maxLen = len(mapPeople[key])
    for key in mapPeople.keys():
        if len(mapPeople[key]) < maxLen:
            for i in range(maxLen - len(mapPeople[key])):
                mapPeople[key] += "2"
        listValue.append(mapPeople[key])

    listValue = sorted(listValue)
    listkey = sorted(listkey)

    for key in listkey:
        index = listValue.index(mapPeople[key])
        listSort[index] = key
        listValue[index] = ""

    for i in range(len(listSort)):
        print(listSort[i] + "\n")
    print("==============================")

main()
