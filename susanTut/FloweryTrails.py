class Node(object):
    """
    The nodeName will be the number marked with the node
    """
    def __init__(self, nodeName):
        self.nodeName = nodeName
        # nodeTo is a list with length numNode, and use index as the name of the name, and value for each index will be a list containing
        # the length of way to go the that node, and the number of items in the list is that much of same length way.
        # Example: 1 to 2 have 5 ways, 3 ways with length 20 and the rest is higher than 20, so there will be 3 elements with value 20 in
        # the list at index 2 of nodeTo
        self.nodeTo = [[0] for x in range(numNode)]



listNode = []
numNode = 0
numWayFromNode = [0 for x in range(10000)]
listLength =[]

def getInput():
    global listNode, numNode
    numNode_direction = input().split()
    numNode = int(numNode_direction[0])
    listNode = [Node(x) for x in range(numNode)]
    directions = int(numNode_direction[1])
    for i in range(directions):
        inputString = input().split()
        in1 = int(inputString[0])
        in2 = int(inputString[1])
        in3 = int(inputString[2])
        if in1 == in2:
            pass
        else:
            listNode[in1].nodeName = int(in1)
            if listNode[in1].nodeTo[in2] == [0] or listNode[in1].nodeTo[in2][0] > in3:
                listNode[in1].nodeTo[in2] = []
                listNode[in1].nodeTo[in2].append(in3)
            elif listNode[in1].nodeTo[in2][0] == in3:
                listNode[in1].nodeTo[in2].append(in3)

            listNode[in2].nodeName = int(in2)
            if listNode[in2].nodeTo[in1] == [0] or listNode[in2].nodeTo[in1][0] > in3:
                listNode[in2].nodeTo[in1] = []
                listNode[in2].nodeTo[in1].append(in3)
            elif listNode[in2].nodeTo[in1][0] == in3:
                listNode[in2].nodeTo[in1].append(in3)


def findSimilarTracks():
    return None

def goAlongRoute(node):
    global numNode
    if node.nodeName>=numNode-1:
        return 0
    index = node.nodeName+1
    while node.nodeTo[index] == [0] and index<numNode-1:
        index += 1
    return len(node.nodeTo[index])*node.nodeTo[index][0]+goAlongRoute(listNode[index])

def traversal(node):
    global listLength, numNode

    for i in range(1,len(listNode)):
        length = 0
        if node.nodeTo[i] != [0]:
            length += len(node.nodeTo[i])*node.nodeTo[i][0]+goAlongRoute(listNode[i])
        if length!=0:
            listLength.append(length)

    minLength = min(listLength)
    result = listLength.count(minLength)*minLength*2

    return result



if __name__ == '__main__':
    getInput()
    print(listNode)
    for node in listNode:
        print(node.nodeTo)

    print(traversal(listNode[0]))
    print(listLength)
