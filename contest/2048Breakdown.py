def inp():
    mapLine = {}
    line1 = input().split()
    line2 = input().split()
    line3 = input().split()
    line4 = input().split()
    listLine = [line1,line2,line3,line4]
    direction = int(input())
    for i in range(4):
        mapLine[i] = [int(x) for x in listLine[i]]
    return (mapLine,direction)

def main():
    inData = inp()
    mapLines = inData[0]
    direction = inData[1]

def move_left(mapLines):
    for line in range(4):
        newLine = [x for x in mapLines[line] and x!=0]
        for index in range(1,len(newLine)):
            if newLine[index] == newLine[index-1]:
                mapLines[line][index-1] *= 2
                # mapLines[line][index] =
