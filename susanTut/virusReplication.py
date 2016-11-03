def getInput():
    original_DNA = input()
    infected_DNA = input()

    return (original_DNA,infected_DNA)

def process(input_DNAs):
    original_DNA = input_DNAs[0]
    infected_DNA = input_DNAs[1]
    front_diff = -1
    end_diff = -1
    for front, end, end_original, front_original in zip(range(len(infected_DNA)), range(len(infected_DNA)-1,-1,-1), range(len(original_DNA)-1,-1,-1), range(len(original_DNA))):
        # print(front)
        # print(end)
        # print()
        if front < len(original_DNA):
            if front_diff == -1 and original_DNA[front] != infected_DNA[front]:
                front_diff = front
            if end_diff == -1 and original_DNA[end_original] != infected_DNA[end]:
                end_diff = end
            if front_diff != -1 and end_diff != -1:
                break

    print((front_diff,end_diff))
    if front_diff == -1 and end_diff == -1:
        if len(original_DNA) == len(infected_DNA):
            return 0
        else:
            return abs(len(original_DNA)-len(infected_DNA))
    elif front_diff == end_diff:
        if len(original_DNA) == len(infected_DNA):
            return 1
        else:
            return abs(len(original_DNA)-len(infected_DNA))
    elif front_diff == 0:
        return abs(end_diff-front_diff)
    else:
        return abs(end_diff-front_diff)+1

if __name__ == '__main__':
    result = process(getInput())
    print(result)