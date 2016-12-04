def knapsack_solving_dp(arrayItems, capacity):
    result = [[0 for i in range(capacity + 1)]]
    for i in range(len(arrayItems)):
        result.append([0])
    # print_map(result)
    for row in range(1, len(arrayItems) + 1):
        for col in range(1, len(result[0])):
            if col - arrayItems[row - 1][0] < 0:
                result[row].append(result[row - 1][col])
            else:
                result[row].append(
                    max(result[row - 1][col], result[row - 1][col - arrayItems[row - 1][0]] + arrayItems[row - 1][1]))
        # print_map(result)
                # print(col)
    return result[-1][-1]


def print_map(anMap):
    for lst in anMap:
        print(lst)


if __name__ == '__main__':
    print(knapsack_solving_dp([(2, 12), (1, 10), (3, 20), (2, 15)], 5))

