# Idea: Using a while loop loop through the input list until the input list is empty. Eveytime in the while loop, calculate all possible case
# of event that 1 single server can handle, then add up the number of server, eliminate all the event that server can handle in the list, and move on.
import time

listRequest = []
capacity = 0
numRequest = 0
checkList = []

def getinput():
    global listRequest, capacity, numRequest, checkList

    # begin = time.time()
    numRequestAndCapacity = input().split()
    numRequest = int(numRequestAndCapacity[0])
    capacity = int(numRequestAndCapacity[1])
    for i in range(numRequest):
        listRequest.append(int(input()))
        checkList.append(-1)
    # print(time.time()-begin)

def checkserver():
    global listRequest, capacity, checkList
    firstSkip = 0
    for server in range(capacity):
        lastIndex = 0
        if listRequest != checkList:
            limitTime = listRequest[firstSkip]

            for i in range(lastIndex,len(listRequest)):
                if listRequest[i] >= limitTime:
                    limitTime = listRequest[i]+1000
                    listRequest[i] = -1
                    lastIndex = i
                if listRequest[firstSkip] == -1:
                    firstSkip = i+1
        else:
            break
    return lastIndex

if __name__ == '__main__':
    # begin = time.time()
    getinput()
    numServer = 0

    while listRequest != checkList:
        # print(listRequest)
        checkserver()
        numServer += 1

    # for i in range(100000):
    #     print(i)

    print(numServer)
    # print(time.time()-begin)