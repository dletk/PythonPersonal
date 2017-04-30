def answer1(l):
    result = []
    finalResult = []
    for version in l:
        listForm = version.split(".")
        tupVersion = tuple(listForm)
        if len(tupVersion) == 1:
            tupVersion = (tupVersion[0], 0, 0)
        elif len(tupVersion) == 2:
            tupVersion = (tupVersion[0], tupVersion[1], 0)
        tupVersion = (tupVersion[0], tupVersion[1], tupVersion[2], len(listForm))
        result.append(tupVersion)
    for tup in sorted(result, key = lambda x: (int(x[0]), int(x[1]), int(x[2]), x[3])):
        out = ""
        for ind in range(tup[3]):
            out += tup[ind]
            out += "."
        finalResult.append(out.rstrip("."))
    return finalResult

def answer2(h, q):
    # Idea: Check top down, see if the number in q+1/q+2 is equal to h-1/2 or not
    # if not, then continue until found it is equal, then that
    # current value of h is the parent
    maxValue = 2**h-1
    result = []
    for num in q:
        if num == maxValue:
            result.append(-1)
        else:
            found = False
            checkMax = maxValue
            while not found:
                if num + 2 == checkMax or num*2+1 == checkMax:
                    result.append(checkMax)
                    found = True
                else:
                    if num <= (checkMax-1)//2:
                        checkMax = (checkMax-1)//2
                    else:
                        checkMax -= 1
    return result

def answer(h, q):
    highestValue = 2**h -1
    result = []
    for num in q:
        maxVal = highestValue
        minVal = 1
        if num == maxVal:
            result.append(-1)
        else:
            found = False
            lastMax = maxVal
            while not found:
                print(maxVal)
                print(num)
                if minVal + (maxVal-minVal)//2 > num:
                    lastMax = maxVal
                    maxVal = minVal + (maxVal-minVal)//2 - 1
                else:
                    minVal += (maxVal-minVal)//2
                    maxVal -= 1
                if maxVal == num:
                    found = True
                    # if maxVal == num:
                    #     result.append(lastMax)
                    # else:
                    result.append(maxVal)


    return result

if __name__ == '__main__':
    # print(answer(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
    # print(answer(30, [1,4,7, 1073741793]))
    print(answer(3, [7,3,5,1]))
    print(answer(5, [19,14,28]))
    # print(answer(30, [1,4,7, 1073741793]))
    # print(answer(30, [1,4,7, 1073741793]))