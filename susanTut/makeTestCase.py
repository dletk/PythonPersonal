import random

def makeTestCaseForSubsequence():
    # random.seed(0)
    listTest = [random.randint(-20000, 20000) for _ in range(100)]
    file = open("test.txt","w")
    for num in listTest:
        file.write(str(num)+" ")
    file.close()

def makeTestCaseForGold():
    """The test generator for getting gold problem. Generate 1 as P, 2 as T, 3 as G, 4 as ."""
    file = open("test.txt","w")
    w = 48
    h = 48
    # The range below is the result of w x h
    listTest = [random.randint(2, 4) for _ in range(w*h)]
    for num in range(len(listTest)):
        file.write(str(listTest[num]))
        if (num+1)%w == 0:
            file.write("\n")
    file.close()

def makeTestCaseBusNumber():
    file = open("test.txt","w")
    listNum = [random.randint(1,1000) for _ in range(1000)]
    for num in listNum:
        file.write(" "+str(num))
    file.close()

if __name__ == '__main__':
    # makeTestCaseForGold()
    makeTestCaseBusNumber()