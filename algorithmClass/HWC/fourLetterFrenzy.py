def inputProcess(file):

    aFile = open(file, "r")
    listWord = []
    for line in aFile:
        listWord.append(line.strip())
    aFile.close()

    dictWords = {}
    for word in listWord:
        dictWords[word] = []
        for wordCompare in listWord:
            if isLinked(word, wordCompare):
                dictWords[word].append(wordCompare)
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

def transform(begin, end, dictWords):
    visited = []
    return transformWordBFS(begin, end, dictWords, visited)

def transformWordBFS(begin,end, dictWords, visited):
    visited.append(begin)
    aQueue = [begin]
    parent = {}
    while aQueue:
        for word in dictWords[aQueue[0]]:
            if word not in visited:
                visited.append(word)
                aQueue.append(word)
                parent[word] = aQueue[0]
                if word==end:
                    return backtrace(parent,begin,end)
        aQueue = aQueue[1:]

def transformDFS(begin, end, dictWords, visited, potential_ans):
    visited.append(begin)
    potential = [begin]
    for word in dictWords[begin]:
        if word not in visited:
            if word==end:
                return potential_ans+potential
            else:
                potentialAns = transformDFS(word,end,dictWords,visited,potential)
                if potentialAns[len(potentialAns)-1]==end:
                    return potential_ans+potentialAns
                else:
                    return potentialAns


def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

if __name__ == '__main__':
    dictWords = inputProcess("fourletterwords.txt")
    # print(dictWords["LOWS"])
    # print(dictWords["COAT"])
    # # print(dictWords["CHAT"])
    # print(dictWords["CHAP"])
    # # print(dictWords["CHIP"])
    # print(dictWords)

    print(transform("BOAT","SHIP",dictWords))
