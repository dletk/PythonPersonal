def changeMaking(denoArray, n):
    listChange = [0]
    for amount in range(1, n + 1):
        tempMin = 999999
        index_deno = 0
        while index_deno < len(denoArray) and amount >= denoArray[index_deno]:
            tempMin = min(listChange[amount - denoArray[index_deno]], tempMin)
            index_deno += 1
        listChange.append(tempMin + 1)
    return listChange[-1]

if __name__ == '__main__':
    denoArray = [1,3,4]
    print(changeMaking(denoArray, 15))