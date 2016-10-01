def main():
    recurs(14)


def recurs(num):
    if num <= 0:
        print("Done")
        return 0
    elif num % 2 == 0:
        n = recurs(num - 1) * 2
        print(n)
        return n
    else:
        n = recurs(num - 1) + 4
        print(n)
        return n


main()
