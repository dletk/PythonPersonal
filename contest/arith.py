def inp():
    num_cases = int(input())
    data = []
    for _ in range(num_cases):
        line = input()
        seq = line.split(" ")
        data.append([int(i) for i in seq[1::]])
    return data


def arithmetic(seq):
    if len(seq) <= 2:
        return True
    diff = seq[1] - seq[0]
    for i in range(len(seq) - 1):
        if seq[i+1] - seq[i] != diff:
            return False
    return True


def main():
    data = inp()
    for seq in data:
        if arithmetic(seq):
            print("arithmetic")
        elif arithmetic(sorted(seq)):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")

main()
