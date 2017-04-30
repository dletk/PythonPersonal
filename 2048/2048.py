import random

cols = [[], [], [], []]
rows = [[], [], [], []]


def generate_map():
    global cols, rows
    for col in cols:
        for i in range(4):
            col.append(0)
    for row in rows:
        for i in range(4):
            row.append(0)
    firstPosition = str(random.randrange(4)) + str(random.randrange(4))
    secondPosition = str(random.randrange(4)) + str(random.randrange(4))
    while secondPosition == firstPosition:
        secondPosition = str(random.randrange(4)) + str(random.randrange(4))
    firstValue = random.randrange(2,5,2)
    secondValue = random.randrange(2,5,2)
    cols[int(firstPosition[:1:])][int(firstPosition[1::])] = firstValue
    cols[int(secondPosition[:1:])][int(secondPosition[1::])] = secondValue
    print(firstPosition)
    print(secondPosition)
    rows = sync_cols_rows(cols, rows)


def sync_cols_rows(sample, modified):
    """
    This method will make "modified" to be the same content as "sample". Cols and Rows will alternatively be sample and modifed
    :param sample: The one to use as sample, will not be changed
    :param modified: The one will be changed accordingly to sample
    :return: The new modified
    """
    for x in range(4):
        for y in range(4):
            modified[x][y] = sample[y][x]

    return modified


def merge_tiles(direction):
    if direction == "u":
        merge_up()
    elif direction == "d":
        merge_down()
    elif direction == "l":
        merge_left()
    else:
        merge_right()


def merge_up():
    global rows, cols
    cols = exclude_zero(cols)
    cols = add_tiles("front", cols)
    cols = exclude_zero(cols)
    cols = put_back_zero("back", cols)
    rows = sync_cols_rows(cols, rows)


def merge_down():
    global rows, cols
    cols = exclude_zero(cols)
    cols = add_tiles("back", cols)
    cols = exclude_zero(cols)
    cols = put_back_zero("front", cols)
    rows = sync_cols_rows(cols, rows)



def merge_left():
    global rows, cols
    rows = exclude_zero(rows)
    rows = add_tiles("front", rows)
    rows = exclude_zero(rows)
    rows = put_back_zero("back", rows)
    cols = sync_cols_rows(rows, cols)



def merge_right():
    global rows, cols
    rows = exclude_zero(rows)
    rows = add_tiles("back", rows)
    rows = exclude_zero(rows)
    rows = add_tiles("front", rows)
    cols = sync_cols_rows(rows, cols)



def exclude_zero(lst):
    """
    This function return the list of columns or rows, with all the number different than 0 is condensed to back or front
    :param lst: list of columns or rows to be modified
    
    :return the lst after being modifed
    """
    for i in range(4):
        newLst = [ele for ele in lst[i] if ele != 0]
        lst[i] = newLst
    return lst


def put_back_zero(position, lst):
    """
    This function return the list of columns or rows, with all the number different than 0 is condensed to back or front
    :param position: The position to put back the 0
    :param lst: The list of columns or rows to be modified
    :return: the lst after being modified
    """
    for i in range(4):
        newLst = lst[i]
        while len(newLst) < 4:
            # Direction "back" mean append to the end, "front" mean append to front
            # TODO: Before putting back the 0s, remember all the position of 0s to randomly generate a new 2/4 later on.
            if position == "back":
                newLst.append(0)
            else:
                newLst = [0] + newLst
        lst[i] = newLst
    return lst


def add_tiles(direction, lst):
    for i in range(4):
        if direction == "front":
            if len(lst[i]) != 1:
                # Loop from the beginning to the end - 1 position of the col/row
                for index in range(len(lst[i])-1):
                    if lst[i][index] == lst[i][index+1]:
                        lst[i][index] = lst[i][index] + lst[i][index+1]
                        lst[i][index+1] = 0
        else:
            if len(lst[i]) != 1:
                # Loop through from the end-1 to beginning position
                for index in range(len(lst[i]) - 1, 0, -1):
                    if lst[i][index] == lst[i][index - 1]:
                        lst[i][index] = lst[i][index] + lst[i][index - 1]
                        lst[i][index - 1] = 0
    return lst


def gamePlay():
    for i in range(4):
        print(rows[i])
    # TODO: Create a method to generate a new 2 or 4 after each move

if __name__ == '__main__':
    exampleList = [[2,2,4], [2], [4,4,2,2], [2,2]]
    assert (put_back_zero("front", exampleList) == [[0,2,2,4], [0,0,0,2], [4,4,2,2], [0,0,2,2]])
    exampleList = [[2,2,4], [2], [4,4,2,2], [2,2]]
    assert (put_back_zero("back", exampleList) == [[2,2,4,0], [2,0,0,0], [4,4,2,2], [2,2,0,0]])
    assert (add_tiles("front", [[2,2,4,0], [2,0,0,0], [4,4,2,2], [2,2,0,0]]) == [[4,0,4,0], [2,0,0,0], [8,0,4,0], [4,0,0,0]])
    assert (add_tiles("back", [[2,2,4,0], [2,0,0,0], [4,4,2,2], [2,2,0,0]]) == [[0,4,4,0], [2,0,0,0], [0,8,0,4], [0,4,0,0]])
    print("All tested passed!!!")
    generate_map()
    print(cols)
    # gamePlay()
    print("----")
    merge_down()
    gamePlay()
