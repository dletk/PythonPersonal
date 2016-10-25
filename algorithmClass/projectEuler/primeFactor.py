import math

def primeFactor(inValue):
    limit = int(inValue/2)+1
    for index in range(limit+1,1,-1):
        if inValue%index==0:
            if checkPrime(index):
                return index


def checkPrime(num):
    limit = int(math.sqrt(num))
    for i in range(limit+1,1):
        if num%i==0 and i!=1:
            return False
    return True

if __name__ == '__main__':
    print(primeFactor(600851475143))