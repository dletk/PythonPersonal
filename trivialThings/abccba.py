def solution():
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            for c in  range(9, -1, -1):
                abccba = a*100000 + b*10000 + c*1000 + c*100 + b*10 + a
                for divider in range(999, 99, -1):
                    if abccba % divider == 0:
                        if len(str(abccba // divider)) == 3:
                            print(divider)
                            return abccba

if __name__ == '__main__':
    print(solution())