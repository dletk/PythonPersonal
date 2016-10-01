def main():
    print(comparisonCoutingSort([99,1,14,29,20]))

def comparisonCoutingSort(a):
    count = []
    sort = [];
    for i in range(len(a)):
        count.append(0)
        sort.append(-1)

    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] < a[j]:
                count[j] = count[j] + 1
            else:
                count[i] = count[i] + 1
    for i in range(len(a)):
        pos = count[i]
        sort[pos] = a[i]

    return sort

main()