import time

def inputProcess(file):

    aFile = open(file, "r")
    setWord = set([])
    for line in aFile:
        setWord.add(line.strip())
    aFile.close()

    dictWords = {}
    for word in setWord:
        dictWords[word] = randomnizeWord(word, setWord)
    return dictWords


def isLinked(word1, word2):
    count = 0
    if word1==word2:
        return False
    for i in range(4):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False


def randomnizeWord(word, setWord):
    listWord = []
    for index in range(len(word)):
        for replace in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            newWord = word[:index]+replace+word[index+1:]
            if newWord in setWord and newWord!=word:
                listWord.append(newWord)
    return listWord


def transform(begin, end, dictWords):
    visited = []
    return transformWordBFS(begin, end, dictWords, visited)


def transformWordBFS(begin,end, dictWords, visited):
    begin = begin.upper()
    end = end.upper()
    if begin not in dictWords:
        print("The starting word is not in the dictionary")
        return None
    elif end not in dictWords:
        print("The ending word is not in the dictionary")
        return None
    visited.append(begin)
    aQueue = [begin]
    parent = {}
    while aQueue:
        for word in dictWords[aQueue[0]]:
            if word not in visited and similarity(word,end):
                visited.append(word)
                aQueue.append(word)
                parent[word] = aQueue[0]
                # potential_ans.append(word)
                if word==end:
                    return findingRoute(parent,begin,end)
        aQueue = aQueue[1:]


def findingRoute(parent, start, end):
    path = [end]
    # print(parent)
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def similarity(word1, word2):
    for i in range(4):
        if word1[i]==word2[i]:
            return True
    return False

if __name__ == '__main__':
    dictWords = inputProcess("fourletterwords.txt")
    # print(dictWords["LOWS"])
    # print(dictWords["COAT"])
    # # print(dictWords["CHAT"])
    # print(dictWords["CHAP"])
    # # print(dictWords["CHIP"])
    # print(dictWords)
    begin = time.time()
    print(transform("boat","ship",dictWords))
    print(time.time()-begin)