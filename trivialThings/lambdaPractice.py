def practiceFunction():
    dictWord = {"a":1,"b":2,"c":3,"d":4}
    listEmpty = [item for item in map(lambda x,y: dictWord[x]+dictWord[y], dictWord.keys(), dictWord.keys())]
    print(listEmpty)

if __name__ == '__main__':
    practiceFunction()