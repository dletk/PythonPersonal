import random

if __name__ == '__main__':
    fileOut = open("output.txt", "w")
    for i in range(100):
        fileOut.write(str(random.randint(0, 100000)))
        fileOut.write(" ")
    fileOut.close()
