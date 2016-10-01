import sys

sys.setrecursionlimit(3000)


def inp():
    data = {}
    for i in range(4):
        line = input()
        line_lst = line.split(" ")
        lst_int = [int(i) for i in line_lst]
        for j in range(4):
            data[i, j] = (lst_int[j])
    move = int(input())
    return data, move


def move_end(seq):
    print(seq)
    if len(seq) <= 1:
        return seq
    if seq[-1] == 0:
        return [0] + move_end(seq[:-1])
    if seq[-2] == 0:
        return [0] + move_end(seq[:-2] + [seq[-1]])
    if seq[-2] != seq[-1]:
        return move_end(seq[:-1]) + [seq[-1]]
    if seq[-2] == seq[-1]:
        return [0] + move_end(seq[1:-1]) + [seq[-2] * 2]


def main():
    dict, move = inp()
    out(dict)
    if move == 0:
        for i in range(4):
            seq = [dict[i, j] for j in range(4)]
            seq.reverse()
            new_seq = move_end(seq).reverse()
            for j in range(4):
                dict[i, j] = new_seq[j]
    elif move == 2:
        for i in range(4):
            seq = [dict[i, j] for j in range(4)]
            new_seq = move_end(seq)
            for j in range(4):
                dict[i, j] = new_seq[j]
    elif move == 3:
        for j in range(4):
            seq = [dict[i, j] for i in range(4)]
            seq.reverse()
            new_seq = move_end(seq).reverse()
            for i in range(4):
                dict[i, j] = new_seq[i]
    else:
        for j in range(4):
            seq = [dict[i, j] for i in range(4)]
            new_seq = move_end(seq)
            for i in range(4):
                dict[i, j] = new_seq[i]
    out(dict)


def out(dict):
    for i in range(4):
        s = ""
        for j in range(4):
            s += str(dict[i, j]) + " "
        print(s)

main()
