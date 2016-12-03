def robot_coin_collect(coinMap):
    results = [[coinMap[0][0]]]
    for index in range(1, len(coinMap)):
        results.append([coinMap[0][index-1]+coinMap[0][index]])
    for index in range(1, len(coinMap[0])):
        results[index].append(coinMap[index-1][0])
    for index_col in range(1, len(coinMap)):
        for index_row in range(1, len(coinMap[0])):
            results[index_row].append(max(results[index_row-1][index_col], results[index_row][index_col-1]+coinMap[index_row][index_col]))
    return results[-1][-1]

if __name__ == '__main__':
    print(robot_coin_collect([[0,0,1],[1,0,1],[0,0,1]]))