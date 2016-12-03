def getInput():
    numCase = int(input())
    for case in range(numCase):
        initial = input().split()
        stack_id = [initial[1]]
        process_passes(stack_id, int(initial[0]))


def process_passes(stack_id, numPasses):
    for index in range(numPasses):
        aPass = input().split()
        lastID = stack_id[-1]
        if aPass[0] == "P":
            lastID = stack_id[-1]
            stack_id.append(aPass[1])
        else:
            temp = stack_id.pop()
            stack_id.append(lastID)
            lastID = temp
    print("Player " + stack_id.pop())


getInput()
