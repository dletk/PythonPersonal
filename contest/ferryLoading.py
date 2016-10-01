def main():
    """Take input"""
    numTestCase = int(input())
    for numCase in range(numTestCase):
        testCase = input()
        listCar = []
        testCaseList = testCase.split()
        length = int(testCaseList[0])*100
        numCar = int(testCaseList[1])
        for num in range(numCar):
            carIn = input()
            carInList = carIn.split()
            listCar.append((int(carInList[0]),carInList[1]))
        leftList = [i[0] for i in listCar if i[1] == "left" and i[0]<=length]
        rightList = [j[0] for j in listCar if j[1] == "right" and j[0]<=length]
        countLeft = 0
        sumL = 0
        for index in range(len(leftList)):
            sumL += leftList[index]
            # print(sumL)
            # print(length)
            if sumL > length:
                countLeft += 1
                if index+1 >= len(leftList):
                    countLeft += 1
                    break
                sumL = leftList[index]
        countRight = 0
        # print(countLeft)
        sumR = 0
        for index in range(len(rightList)):
            sumR += rightList[index]
            if sumR > length:
                countRight += 1
                if index + 1 >= len(rightList):
                    countRight += 1
                    break
                sumR = rightList[index]
        # print(countRight)
        if countLeft > countRight:
            print(2*(countLeft-1)+1)
        elif countLeft < countRight:
            print(countRight*2)
        else:
            print(countLeft*2)
        # print(listCar)

main()