def getInput():
    original_DNA = input()
    infected_DNA = input()

    return (original_DNA,infected_DNA)

def process(input_DNAs):
    original_DNA = input_DNAs[0]
    infected_DNA = input_DNAs[1]
    length_ori = len(original_DNA)
    length_inf = len(infected_DNA)
#     Case 1: len orgininal == len infected
    if length_ori == length_inf:
        front = -1
        end = -1
        for index_front, index_end in zip(range(length_ori),range(length_ori-1,-1,-1)):
            if original_DNA[index_front] != infected_DNA[index_front] and front == -1:
                front = index_front
            if original_DNA[index_end] != infected_DNA[index_end] and end == -1:
                end = index_end
            if end != -1 and front != -1:
                break
        if end == -1 and front == -1:
            return 0
        else:
            return end - front + 1
    # Case 2: len original > len_inf
    elif length_ori > length_inf:
        front = -1
        end = -1
        for index in range(length_inf):
            if original_DNA[index] != infected_DNA[index]:
                front = index
                break
        if front != -1:
            new_inf = infected_DNA[:front:-1]
            for index in range(len(new_inf)):
                if new_inf[index] != original_DNA[length_ori-index-1]:
                    end = length_inf - index - 1
                    break
        if front == -1 or end == -1:
            return 0
        else:
            return end - front + 1
#     Case 3: len ori < len inf
    else:
        front = -1
        end = -1
        for index in range(length_ori):
            if original_DNA[index] != infected_DNA[index]:
                front = index
                break
        if front != -1:
            new_ori = original_DNA[:front:-1]
            for index in range(len(new_ori)):
                if new_ori[index] != infected_DNA[length_inf-index-1]:
                    end = length_ori-index-1
                    break
        if front == -1 or end == -1:
            return length_inf - length_ori
        elif end != -1:
            return length_inf - length_ori + (end - front + 1)


if __name__ == '__main__':
    result = process(getInput())
    print(result)