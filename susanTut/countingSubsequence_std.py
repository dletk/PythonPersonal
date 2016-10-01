def main():
    numCase = int(input())
    listSqus = []
    for time in range(numCase):
        blank = input()
        listSqus.append(int(input()))
        listSqus.append(input())
    for i in range(0,len(listSqus),2):
        seq = list(map(int, listSqus[i+1].split()))
        count = 0
        x = 0
        while x < listSqus[i]:
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
                        x = j + x + 1
                        break
                    if j == newListLen - 1:
                        x += 1
        print(count)

main()
