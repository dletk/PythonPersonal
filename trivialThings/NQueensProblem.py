def main():
    # Take input from user:
    n = int(input("Enter value of n: "))
    placeQueens(n)
    return 0

def placeQueens(n):
    # A map to hold the rows with the key is the index of the row from 0 to n-1
    listOfRow = {}
    # A list to hold position that we are placing the queens correctly. if len(listPos)==8 then we finished.
    listPos = []
    # Fill in the map with square in the form:
    # For row 0, the key is 0, the value is: 0 = ["00","01",...."0n"]
    for i in range(n):
        listOfRow[i] = [str(i)+str(x) for x in range(n)]
    # The while loop is confusing now, not really have a meaning for now.
    while True:
        # Loop through the pos of first row because there need to be 1 queen in this row anyway.
        for pos in listOfRow[0]:
            # Number of queen we have placed on table.
            finishQueen = 1
            listPos.append(pos)
            # Dead position that cannot place the next queen on.
            deadPos = [x for x in listOfRow[0]] + [str(y)+pos[1] for y in range(n)] + []
    return 0

if __name__ == '__main__':
    main()
