import sys

sys.setrecursionlimit(3000)


class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbor = []
        self.visited = False
        self.type = ""
        self.line = -1

    def add_neighbor(self, neighbor):
        self.neighbor.append(neighbor)

    def is_visited(self):
        return self.visited

    def set_visited(self):
        self.visited = True

    def set_line(self, line):
        self.line = line

    def set_type(self, type):
        self.type = type


posSafe = []
posG = []
posT = []
count = 0
mapNodesByLine = {}


def main():
    listInt = input()
    listInt = list(map(int, listInt.split()))

    w = listInt[0]
    h = listInt[1]

    # Variables to hold the input lines
    listLine = []
    global mapNodesByLine
    # List variables to hold the position of G and T, and position of P is a single string because P is unique.
    global posSafe
    global posG
    global posT
    # Map with key is safe position, value is list of its neighbor

    for line in range(h):
        listLine.append(input())
        currLine = listLine[line]
        mapNodesByLine[line] = []

        for index in range(w):
            char = currLine[index]

            newNode = Node(line, index)
            newNode.set_type("#")
            newNode.set_line(line)

            if char == "T":
                newNode.set_type("T")
                mapNodesByLine[line].append(newNode)
            elif char == "G":
                newNode.set_type("G")
                mapNodesByLine[line].append(newNode)
                posG.append(newNode)
            elif char == ".":
                newNode.set_type(".")
                mapNodesByLine[line].append(newNode)
            elif char == "P":
                newNode.set_type("P")
                posP = newNode
                mapNodesByLine[line].append(posP)
            else:
                newNode.set_visited()
                mapNodesByLine[line].append(newNode)

    dfs_recur(posP)
    print(count)


def dfs_recur(node):
    global posG
    global posT
    global count
    global mapNodesByLine

    if node.is_visited():
        return
    else:
        node.set_visited()

    if node.type == "G":
        count += 1

    if 1 <= node.y - 1 < len(mapNodesByLine[node.x]) - 1 and mapNodesByLine[node.x][node.y - 1].type == "T":
        return
    if node.y + 1 < len(mapNodesByLine[node.x]) - 1 and mapNodesByLine[node.x][node.y + 1].type == "T":
        return
    if node.x - 1 >= 1 and node.y < len(mapNodesByLine[node.x - 1]) - 1 and mapNodesByLine[node.x - 1][node.y].type == "T":
        return
    if node.x + 1 < len(mapNodesByLine) - 1 and node.y < len(mapNodesByLine[node.x + 1]) - 1 and mapNodesByLine[node.x + 1][node.y].type == "T":
        return

    if 1 <= node.y - 1 < len(mapNodesByLine[node.x]) - 1:
        if not mapNodesByLine[node.x][node.y - 1].is_visited():
            dfs_recur(mapNodesByLine[node.x][node.y - 1])
    if node.y + 1 < len(mapNodesByLine[node.x]) - 1:
        if not mapNodesByLine[node.x][node.y + 1].is_visited():
            dfs_recur(mapNodesByLine[node.x][node.y + 1])
    if node.x - 1 >= 1 and node.y < len(mapNodesByLine[node.x - 1]) - 1:
        if not mapNodesByLine[node.x - 1][node.y].is_visited():
            dfs_recur(mapNodesByLine[node.x - 1][node.y])
    if node.x + 1 < len(mapNodesByLine) - 1 and node.y < len(mapNodesByLine[node.x + 1]) - 1:
        if not mapNodesByLine[node.x + 1][node.y].is_visited():
            dfs_recur(mapNodesByLine[node.x + 1][node.y])


main()
