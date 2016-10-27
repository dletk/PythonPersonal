# Idea: Using a while loop loop through the input list until the input list is empty. Eveytime in the while loop, calculate all possible case
# of event that 1 single server can handle, then add up the number of server, eliminate all the event that server can handle in the list, and move on.
import queue

listRequest = []
capacity = 0
numRequest = 0
queueServer = queue.PriorityQueue()
queueServer.put((0,[]))
lenQueue = 1
lastAdded = 0

def getinput():
    global listRequest, capacity, numRequest

    # begin = time.time()
    numRequestAndCapacity = input().split()
    numRequest = int(numRequestAndCapacity[0])
    capacity = int(numRequestAndCapacity[1])
    for i in range(numRequest):
        checkserver(int(input()))
    # print(time.time()-begin)

def checkserver(request):
    global queueServer, capacity, lenQueue, lastAdded
    added = False
    server = queueServer.get()
    print(server)
    # print(request)
    if len(server[1])>=capacity:
        for i in range(capacity):
            if server[1][i]+1000 <= request:
                lastAdded += 1
                newList = server[1]
                newList[i] = request
                # server = (server[0],request)
                queueServer.put((lastAdded,newList))
                added = True
                break
    else:
        lastAdded += 1
        newList = server[1]
        newList.append(request)
        server = (lastAdded, newList)
        queueServer.put(server)
        added = True

    if not added:
        queueServer.put((1,[request]))
        lenQueue += 1

    return lenQueue

if __name__ == '__main__':
    # begin = time.time()
    getinput()
    print(lenQueue)

    # while listRequest != checkList:
    #     # print(listRequest)
        # numServer += 1

    # for i in range(100000):
    #     print(i)

    # print(time.time()-begin)