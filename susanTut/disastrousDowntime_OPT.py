listRequest = []
listSecond = [0 for x in range(0, 1001)]
capacity = 0

def getinput():
    global listRequest, capacity, numRequest, listSecond

    numRequestAndCapacity = input().split()
    numRequest = int(numRequestAndCapacity[0])
    capacity = int(numRequestAndCapacity[1])
    for i in range(numRequest):
        request = int(input())
        listRequest.append(request)
        listSecond[request%1000] += 1


def processInput():
    global listRequest, listSecond, capacity
    sumServer = 0
    maxX = max(listSecond)/capacity
    for second in listSecond:
        if second == 1:
            sumServer += 1
        elif second>1:
            sumServer += second-1
    return maxX


if __name__ == '__main__':
    getinput()
    print(processInput())
