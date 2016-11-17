def getInput():
    """
    Get the input from standard input
    :return: the sorted in order of number of all buses
    """
    numBus = int(input())
    listBuses = list(map(int, input().split()))
    listBuses.sort()
    return listBuses


def process():
    """
    Process data
    :return:
    """
    listBuses = getInput()
    arr_result = [listBuses[0]]
    str_result = ""
    for index in range(len(listBuses)):
        if int(listBuses[index]) + 1 != int(listBuses[index + 1]):
            str_result = addToResult(arr_result, str_result)
            arr_result = [listBuses[index + 1]]
        else:
            arr_result.append(listBuses[index + 1])
        if index + 1 == len(listBuses) - 1:
            str_result = addToResult(arr_result, str_result)
            break
    return str_result.lstrip()


def addToResult(arr_result, str_result):
    """

    :param arr_result:
    :param str_result:
    :return:
    """
    if len(arr_result) == 1:
        str_result += " " + str(arr_result[0])
    elif len(arr_result) == 2:
        str_result += " " + str(arr_result[0]) + " " + str(arr_result[-1])
    else:
        str_result += " " + str(arr_result[0]) + "-" + str(arr_result[-1])
    return str_result


if __name__ == '__main__':
    print(process())
