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
        if len(leftList) == 1:
            countLeft = 1
        else:
            for index in range(len(leftList)):
                sumL += leftList[index]
                if sumL > length:
                    countLeft += 1
                    sumL = leftList[index]
                if index+2 >= len(leftList):
                    if leftList[index]+leftList[index+1] >= length:
                        if leftList[index] >= length:
                            countLeft += 2
                        elif leftList[index+1] >= length:
                            countLeft += 2
                        else:
                            countLeft += 2
                    if sumL <= length:
                        countLeft += 2
                        # countLeft += 3
                    break

        countRight = 0
        sumR = 0
        if len(rightList) == 1:
            countRight = 1
        else:
            for index in range(len(rightList)):
                sumR += rightList[index]
                if sumR > length:
                    countRight += 1
                    sumR = rightList[index]
                if index + 2 >= len(rightList):
                    if rightList[index] + rightList[index + 1] >= length:
                        if rightList[index] >= length:
                            countRight += 2
                        elif rightList[index + 1] >= length:
                            countRight += 2
                        else:
                            countRight += 2
                    if sumR <= length and sumR+rightList[index+1]>= length or rightList[index+1]>= length:
                        countRight += 2
                    elif sumR <= length:
                        countRight += 1
                            # countLeft += 3
                    break
        # print(countRight)
        if countLeft > countRight:
            print(2*(countLeft-1)+1)
        elif countLeft < countRight:
            print(countRight*2)
        else:
            print(countLeft*2)
        # print(listCar)

main()