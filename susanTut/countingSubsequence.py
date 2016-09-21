import time

def main():

    file = open("test.in", "r")

    rawInptList = file.readlines()
    file.close()
    numCase = int(rawInptList[0])
    timeNow = time.time()
    for i in range(2, 3 * numCase + 1, 3):
        lengthSeq = int(rawInptList[i])
        seq = list(map(int, rawInptList[i + 1].split()))
        count = 0
        x = 0
        while x < lengthSeq:
            if seq[x] == 47:
                count += 1
                x += 1
            else:
                newList = seq[x:]
                result = 0
                newListLen = len(newList)
                for j in range(newListLen):
                    result += newList[j]
                    if result == 47:
                        count += 1
                        x = j+x+1
                        break
                    if j == newListLen-1:
                        x += 1
                        # print("Check")
        # print("Done")
        print(count)
    print(time.time()-timeNow)

main()
