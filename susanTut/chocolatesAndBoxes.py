def getInput():
    numCase = int(input())
    for case in range(numCase):
        process()


def process():
    checkingSet = {}
    numBox = input()
    listBox = list(map(lambda x: int(x), input().split()))
    numChoco_needed = int(input())
    count = 0
    for box in listBox:
        if numChoco_needed - box in checkingSet:
            count += checkingSet.get(numChoco_needed - box)
        if box not in checkingSet:
            checkingSet[box] = 1
        else:
            checkingSet[box] += 1
    print(count)

getInput()