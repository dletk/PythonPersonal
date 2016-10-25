def pythagorean():
    for a in range(1,800):
        for b in range(1,1000-a+1):
            for c in range(1,1000-a-b+1):
                if a**a+b**b==c**c and a+b+c==1000:
                    return a*b*c

if __name__ == '__main__':
    print(pythagorean())