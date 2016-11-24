def getinput():
    numCase = int(input())
    for case in range(numCase):
        process(input().split())


def process(case):
    if case[0] == 'B':
        decrement(list(map(lambda x: int(x), case[1:])))
    else:
        increment(list(map(lambda x: int(x), case[1:])))


def decrement(case):
    diff = case[-1] - case[0]
    if diff >= 0:
        print(str(case[1]) + " " + str(diff))
    else:
        if abs(diff) > 60:
            hour = case[1] - abs(diff) // 60 - 1
        else:
            hour = case[1] - 1
        if abs(diff) > 60:
            minute = 120 - abs(diff)
        else:
            minute = 60 - abs(diff)
        if hour < 0:
            hour += 24
        print(str(hour) + " " + str(minute))


def increment(case):
    sumMin = case[0] + case[-1]
    if sumMin < 60:
        print(str(case[1]) + " " + str(sumMin))
    else:
        hour = (case[1] + sumMin // 60) % 24
        minute = sumMin % 60
        print(str(hour) + " " + str(minute))


if __name__ == '__main__':
    getinput()
