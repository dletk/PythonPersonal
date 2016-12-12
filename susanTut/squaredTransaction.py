def getInput():
    lengthArray = int(input())
    trans_array = list(map(lambda x: int(x), input().split()))
    numQueries = int(input())
    queries = []
    for query in range(numQueries):
        queries.append(int(input()))
    process(trans_array, queries)


def process(trans_array, queries):
    sumArray = generateSum(trans_array)
    for query in queries:
        print(biSearch(sumArray, query))


def generateSum(trans_array):
    sumArray = [trans_array[0]]
    for index in range(1, len(trans_array)):
        sumArray.append(sumArray[index - 1] + trans_array[index])
    return sumArray


def biSearch(sumArray, query):
    mid = len(sumArray) // 2
    high = len(sumArray) - 1
    low = 0
    resultIndex = -1
    while low <= high:
        if sumArray[mid] == query:
            return mid + 1
        elif sumArray[mid] < query:
            low = mid + 1
            mid = (low + high) // 2
        else:
            resultIndex = mid
            high = mid - 1
            mid = (low + high) // 2
    if resultIndex != -1:
        return resultIndex + 1
    else:
        return -1


getInput()
