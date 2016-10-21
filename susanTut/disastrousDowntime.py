# Idea: Using a while loop loop through the input list until the input list is empty. Eveytime in the while loop, calculate all possible case
# of event that 1 single server can handle, then add up the number of server, eliminate all the event that server can handle in the list, and move on.

listRequest = []
capacity = 0


def getinput():
    global listRequest, capacity

    numRequestAndCapacity = input().split()
    numRequest = int(numRequestAndCapacity[0])
    capacity = int(numRequestAndCapacity[1])
    for i in range(numRequest):
        listRequest.append(int(input()))


def checkserver():
    global listRequest, capacity

    listRemove = []
    indexNextStart = 0
    limitTime = listRequest[indexNextStart]+1000
    serverCapacity = 0

    for request in listRequest:
        print(request)
        print(indexNextStart)
        print(listRemove)
        if request >= limitTime:
            if listRemove[indexNextStart]+1000 <= request:
                if listRemove[indexNextStart]+1000 < limitTime:
                    limitTime = listRemove[indexNextStart]+1000
                serverCapacity -= 1
                indexNextStart += 1

        if request <= limitTime and serverCapacity < capacity:
            listRemove.append(request)
            serverCapacity += 1

        # elif request <= limitTime and serverCapacity == capacity:
        #     if listRemove[indexNextStart]+1000 == limitTime:
        #         pass
        #     else:
        #         limitTime = listRemove[indexNextStart] + 1000
        #         indexNextStart += 1
        #         listRemove.append(request)
        # elif request >= limitTime and serverCapacity == capacity:
        #     if listRemove[indexNextStart]+1000 >= request:
        #         limitTime = listRemove[indexNextStart]+1000
        #         indexNextStart += 1
        #         listRemove.append(request)

    print(listRemove)

    for request in listRemove:
        listRequest.remove(request)


if __name__ == '__main__':
    getinput()
    numServer = 0

    while listRequest!=[]:
        checkserver()
        numServer += 1

    print(numServer)