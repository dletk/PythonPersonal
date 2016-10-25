def sumLimit(limit):
    limit = limit-1
    num3 = limit//3
    num5 = limit//5
    num15 = limit//15
    sumResult = num3*(num3+1)/2*3+num5*(num5+1)/2*5-num15*(num15+1)/2*15

    return sumResult

if __name__ == '__main__':
    print(sumLimit(1000))
