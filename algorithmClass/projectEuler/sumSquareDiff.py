def sumSquareDiff():
    sumSquare = 0
    for i in range(1,101,1):
        sumSquare += i*i
    return (101*50)**2-sumSquare

if __name__ == '__main__':
    print(sumSquareDiff())