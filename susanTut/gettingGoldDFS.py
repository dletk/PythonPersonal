import time
import sys

sys.setrecursionlimit(3000)


class Node(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.neighbor = []
        self.visited = False
    def add_neighbor(self,neighbor):
        self.neighbor.append(neighbor)
    def is_visited(self):
        return self.visited
    def set_visited(self):
        self.visited = True


posSafe = []
posG = []
posT = []
listNode = []
count = 0


def main():
    listInt = input()
    listInt = list(map(int,listInt.split()))

    w = listInt[0]
    h = listInt[1]

    # Variables to hold the input lines
    listLine = []
    # List variables to hold the position of G and T, and position of P is a single string because P is unique.
    global posSafe
    global posG
    global posT
    global listNode
    # Map with key is safe position, value is list of its neighbor
    begin = time.time()
    for line in range(h):
        listLine.append(input())
        currLine = listLine[line]
        if "P" in currLine:
            posP = Node(line,currLine.find("P"))
            listNode.append(posP)
        for index in range(w):
            char = currLine[index]
            if char != "#" and char != "P":
                newNode = Node(line,index)
                listNode.append(newNode)
            if char == "T":
                posT.append(newNode)
            elif char == "G":
                posG.append(newNode)
            elif char == ".":
                posSafe.append(newNode)
    posSafe = posSafe + posG
    posSafe.append(posP)

    begin2 = time.time()
    # 99% of the time from this
    for pos in posSafe:
        for node in listNode:
            if node.x == pos.x and (node.y == pos.y+1 or node.y == pos.y-1):
                pos.add_neighbor(node)
            if node.y == pos.y and (node.x-1 == pos.x or node.x+1 == pos.x):
                pos.add_neighbor(node)
    end = time.time()


    dfs_recur(posP)
    print(count)
    print(time.time()-begin)
    print(end - begin2)

def dfs_recur(node):
    global posG
    global posT
    global count

    if node.is_visited():
        return
    else:
        node.set_visited()

    if node in posG:
        count += 1

    for neighbor in node.neighbor:
        if neighbor in posT:
            return

    for child in node.neighbor:
        if not child.is_visited():
            dfs_recur(child)

main()
# TODO: Create list of each lines, each list containts Node in that line. Each node has inside it an variable "type"
# which value is T, G, P, . and #.
#  Use index of those lines to check for +/-1 to find neighbor instead of the for loop above.