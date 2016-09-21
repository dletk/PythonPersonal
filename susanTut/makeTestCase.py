import random

def main():
    random.seed(0)
    listTest = [random.randint(-20000, 20000) for _ in range(100000)]
    file = open("test.in","w")
    for num in listTest:
        file.write(str(num)+" ")
    file.close()

main()