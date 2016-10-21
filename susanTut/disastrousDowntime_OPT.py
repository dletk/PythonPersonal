# Idea: Using a while loop loop through the input list until the input list is empty. Eveytime in the while loop, calculate all possible case
# of event that 1 single server can handle, then add up the number of server, eliminate all the event that server can handle in the list, and move on.
import time

listRequest = []
capacity = 0
numRequest = 0
listServer = [[]]


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
    global listServer, capacity
    added = False
    for server in listServer:
        if server == [] or len(server) < capacity:
            server.append(request)
            added = True
            break
        elif len(server) == capacity:
            for i in range(len(server)):
                if server[i]+1000 <= request:
                    server[i] = request
                    added = True
                    break
    if not added:
        listServer.append([request])
    # print(listServer)
        # print(listServer)

    return len(listServer)
if __name__ == '__main__':
    # begin = time.time()
    getinput()
    print(len(listServer))

    # while listRequest != checkList:
    #     # print(listRequest)
        # numServer += 1

    # for i in range(100000):
    #     print(i)

    # print(time.time()-begin)