def robot_coin_collect(coinMap):
    result = [[coinMap[0][0]]]
    for index in range(1, len(coinMap[0])):
        result[0].append(result[0][index - 1] + coinMap[0][index])
    for index in range(1, len(coinMap)):
        result.append([result[index - 1][0] + coinMap[index][0]])
    # print_map(result)
    for row in range(1, len(coinMap)):
        for col in range(1, len(coinMap[0])):
            result[row].append(max(result[row - 1][col], result[row][col - 1]) + coinMap[row][col])
    return result[-1][-1]


def print_map(anMap):
    for lst in anMap:
        print(lst)


if __name__ == '__main__':
    print(robot_coin_collect([[0, 0, 1], [1, 0, 1], [0, 0, 1]]))
    print(robot_coin_collect(
        [[0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0]]))
