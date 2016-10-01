def main():
    input = [1, 4, -3, -4, 6, -7, 8, -5]
    map = {}
    sum = 0
    for i in range(len(input)):
        sum += input[i]
        if sum in map:
            print(map[sum][0] + 1, "to", i)
        map[sum] = (i, sum)
    print(map)

main()