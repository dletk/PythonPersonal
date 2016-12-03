def coin_row_solution(anArray):
    if len(anArray) < 3:
        return (max(anArray))
    else:
        results = [anArray[0], max(anArray[0], anArray[1])]
        for index in range(2, len(anArray)):
            results.append(max(results[index - 1], anArray[index] + results[index - 2]))
        return results[-1]

if __name__ == '__main__':
    print(coin_row_solution([9,10,14,2,1,20]))