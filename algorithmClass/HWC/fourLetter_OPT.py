"""Author: Duc Le
Collaborator: Tuyet-Anh Tran

['BOAT', 'BHAT', 'SHAT', 'SHIT', 'SHIP']
['DICK', 'PICK']
['FEET', 'FENT', 'FONT', 'FOOT']
['SHIP', 'SHOP', 'SOOP', 'GOOP', 'GOOD', 'FOOD']
['KICK', 'KECK', 'BECK', 'BEAK', 'BEAT']
['TALK', 'TALL', 'TELL', 'TEAL', 'TEAR']
[start='ISBA', end='KICK'] => None

In the first attempt, I have tried to go through all 4 letter words that are 1-letter-different from the starting words,
and for each word, I recursively kept trying to go through all its 1-letter-different words that is not the original word,
until I found the ending word. This can be considered as a Depth First search for finding the route, and it becomes
incredibly long since there can be a route lead to nowhere and there will be a waste of time traveling down that route and
move on to the next one. Also, this algorithm will not find for me the shortest loop unless some optimization is made.

My final approach can be considered in to 2 stages, processing the input file and transforming the word. For the processing
part, I have a set that contains all words in the input file, and then for each of the words in this set, I put it into
a dictionary with that word be the key and a list of all words that are in the input AND 1-letter-difference with it as
the value. After that, considering this dictionary as a graph, I use the Bread-first-search algorithm, start with the
starting words and search for the ending words. When I found the ending words, I break from the BFS immediately and
print back the route I have go through from the starting word to it. This approach is better than a DFS because it will
 search for the nearest words first, making the found route to be the shortest one, and we do not need to fo along
 a wrong route for too long.

My algorithm has the inputProcess function loop through all the line in the dictionary once, and for each word in it,
I loop thorugh it 4x26 times to create 1-letter-different words.
    => T(n) = n + 104n
Then my transform function will perform a Bread-First search on the graph with vertex are the words in dictionary and edges
are the number of pair of words that are 1-letter-different. So the time complexity function becomes:
    T(n) = n + 104n + V + E
Finally, finding the route by tracing back the BFS will take O(m) time average, with m is the number of nodes on that route.
    T(n) = 105n + V + E + m
Because m is considerably smaller than n, we have
    T(n) = 105n + V + E
On average, if V and E is a multiple of n (which can be not true with a very dense graph), the time complexity of this algorithm
will be O(n).

"""

import queue


def inputProcess(file):
    """
    The function process the input file to make a dictionary with key is the word in the file, value is a list of of all
    words that is 1-letter-different with it in the input file.
    :param file: The input file name
    :return: the dictionary with key is a word in input file, value is a list of 1-letter-different words from it.
    """

    aFile = open(file, "r")
    setWord = set([])
    for line in aFile:
        setWord.add(line.strip())
    aFile.close()

    dictWords = {}
    for word in setWord:
        dictWords[word] = randomnizeWord(word, setWord)
    return dictWords


def randomnizeWord(word, setWord):
    """
    Create all the possible 1-letter-different words of the input word, and add it to the output list if that word is in
    the input file
    :param word: the key word
    :param setWord: the set of words in input file
    :return: a list of 1-letter-different words from the input word
    """
    listWord = []
    for index in range(len(word)):
        for replace in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            newWord = word[:index]+replace+word[index+1:]
            if newWord in setWord and newWord!=word:
                listWord.append(newWord)
    return listWord


def transform(begin, end, dictWords):
    """
    Function to begin transform the begin word to the end words, using the dictionary created by the input file.
    :param begin: the beginning word
    :param end: the ending word
    :param dictWords: the dictionary of word and list of words its connected to, from the input file.
    :return: the path of of how to transform begin to end in the form of a list, or None if begin cannot be transformed to end
    """
    visited = set()
    return transformWordBFS(begin, end, dictWords, visited)


def transformWordBFS(begin,end, dictWords, visited):
    """
    Conducting Bread First Search on the graph with vertex are the key in the dictionary dictWords to find the path to
    transform begin to end.
    :param begin: the beginning word
    :param end: the ending word
    :param dictWords: the dictionary of word and list of words its connected to, from the input file.
    :param visited: the set of visited key.
    :return: a list containing all the key words to transform begin to end.
    """
    begin = begin.upper()
    end = end.upper()
    if begin not in dictWords:
        print("The starting word is not in the dictionary")
        return None
    elif end not in dictWords:
        print("The ending word is not in the dictionary")
        return None
    visited.add(begin)
    aQueue = queue.Queue()
    aQueue.put(begin)
    parent = {}
    while not aQueue.empty():
        head = aQueue.get()
        for word in dictWords[head]:
            if word not in visited:
                visited.add(word)
                aQueue._put(word)
                parent[word] = head
                if word==end:
                    return findingRoute(parent,begin,end)


def findingRoute(parent, start, end):
    """
    Finding the entire route from the ending word back to the starting word.
    :param parent: the parent
    :param start:
    :param end:
    :return:
    """
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


if __name__ == '__main__':
    dictWords = inputProcess("fourletterwords.txt")
    print(transform("boat","ship",dictWords))
    print(transform("dick","pick",dictWords))
    print(transform("feet","foot",dictWords))
    print(transform("ship","food",dictWords))
    print(transform("kick","beat",dictWords))
    print(transform("talk","tear",dictWords))
    print(transform("isba", "kick", dictWords))
