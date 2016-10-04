def kth(inList, num):
    if len(inList) == 0:
        return []
    return inList[num-1:num]+(kth(inList[num:], num))


def isPalindrome(aString):
    length = len(aString)
    if length == 0:
        return True
    return aString[0]==aString[length-1] and isPalindrome(aString[1:length-1])


def isAnagram(word1,word2):
    if len(word1) != len(word2):
        return False
    word1 = sorted(word1)
    word2 = sorted(word2)
    # print(word1 + " " + word2)
    return word1 == word2

if __name__ == '__main__':
    print(kth([3, 4, 1, 3], 1))
    print(kth([3, 4, 1, 3], 2))
    print(kth([3, 4, 1, 3], 3))
    print(kth([3, 4, 1, 3], 4))
    print(kth([3, 4, 1, 3], 5))
    print("==============================")
    print("Test for isPalindrome")
    print(isPalindrome(""))
    print(isPalindrome('f'))
    print(isPalindrome('fo'))
    print(isPalindrome('ff'))
    print(isPalindrome('fof'))
    print(isPalindrome('foof'))
    print(isPalindrome('forf'))
    print("==============================")
    print("Test for isAnagram")
    print(isAnagram("car","arc"))
    print(isAnagram("food","doof"))
    print(isAnagram("food","ddof"))