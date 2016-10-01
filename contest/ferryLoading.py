def inp():
    numTestCase = int(input())
    data = []
    for numCase in range(numTestCase):
        testCase = input()
        listCar = []
        testCaseList = testCase.split()
        length = int(testCaseList[0]) * 100
        numCar = int(testCaseList[1])
        for num in range(numCar):
            carIn = input()
            carInList = carIn.split()
            listCar.append((int(carInList[0]), carInList[1]))
        leftList = [i[0] for i in listCar if i[1] == "left" and i[0] <= length]
        rightList = [j[0] for j in listCar if j[1] == "right" and j[0] <= length]
        lst = (leftList, rightList, length)
        data.append(lst)
    return data


def count_ferries(seq, length):
    count = 1
    s = 0
    for index in range(len(seq)-1):
        s += seq[index]
        if s + seq[index + 1] > length:
            count += 1
            s = 0
    return count


def main():
    """Take input"""
    data = inp()
    for case in data:
        countLeft = count_ferries(case[0], case[2])
        countRight = count_ferries(case[1], case[2])
        if countLeft > countRight:
            print(2*(countLeft-1)+1)
        elif countLeft < countRight:
            print(countRight*2)
        else:
            print(countLeft*2)
        # print(listCar)

main()
