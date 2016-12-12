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
    print_map(result)
    # print(col)
    return result[-1][-1]


def print_map(anMap):
    for lst in anMap:
        print(lst)


if __name__ == '__main__':
    # print(knapsack_solving_dp([(2, 12), (1, 10), (3, 20), (2, 15)], 5))
    # print(knapsack_solving_dp([(2, 5), (3, 2), (6, 6), (4, 12), (1, 2)], 10))
    # print(knapsack_solving_dp(
    #     [(12, 26), (29, 77), (25, 38), (20, 37), (12, 28), (18, 38), (14, 59), (25, 59), (21, 53), (15, 40), (28, 58),
    #      (21, 55)], 63))
    # print(knapsack_solving_dp([(27, 56), (40, 42), (35, 41), (41, 76), (26, 45), (27, 31), (33, 20), (23, 53)], 112))
    print(knapsack_solving_dp([(28,63),(15,50),(31,31),(34,50),(25,24),(15,74)],119))