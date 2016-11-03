def getInput():
    original_DNA = input()
    infected_DNA = input()

    return (original_DNA,infected_DNA)

def process(input_DNAs):
    original_DNA = input_DNAs[0]
    infected_DNA = input_DNAs[1]
    min_len = min([len(original_DNA), len(infected_DNA)])
    max_len = max([len(original_DNA), len(infected_DNA)])

    idx_front = -1
    idx_end = min_len

    for idx_ori, idx_inf in zip(range(min_len), range(min_len)):
        if original_DNA[idx_ori] != infected_DNA[idx_inf]:
            idx_front = idx_ori
            break

    for idx_ori, idx_inf in zip(range(len(original_DNA)-1,-1,-1), range(len(infected_DNA)-1,-1,-1)):
        if original_DNA[idx_ori] != infected_DNA[idx_inf]:
            # print(original_DNA[idx_ori])
            # print(infected_DNA[idx_inf])
            # if idx_ori < idx_inf:
            #     idx_end = idx_inf
            # else:
            #     idx_end = idx_ori
            break
    print(idx_front, idx_ori, idx_inf)
    numRemove = idx_ori - idx_front + 1
    numInsert = idx_inf - idx_front + 1
    # print(numRemove)
    # print(numInsert)
    # TODO: idx_inf and idx_front needs to be taken care
    if idx_front == -1 and idx_end == min_len or idx_inf<idx_front:
        return 0
    if numRemove == numInsert and len(original_DNA) != len(infected_DNA):
        return 2
    return numInsert

if __name__ == '__main__':
    print(process(getInput()))
    # lst = [x for x in range(100000)]
    # lst.reverse()