numCase = int(input())
for case in range(numCase):
    numGear = int(input())
    out = (-1, -1)
    for gear in range(numGear):
        listValue = list(map(lambda x: int(x), input().split()))
        current = (gear + 1, (-listValue[1] * listValue[1] - 4 * listValue[0] * listValue[2]) / (listValue[0] * -4))
        if current[1] > out[1]:
            out = current
    print(out[0])
