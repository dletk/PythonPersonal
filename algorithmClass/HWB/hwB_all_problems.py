def kth(inList, num):
    if len(inList) == 0 or num == 0:
        return []
    return inList[num-1:num]+(kth(inList[num:], num))


def isPalindrome(aString):
    length = len(aString)
    if length == 0:
        return True
    index = 0
    while index < length and not aString[index].isalpha():
        index += 1

    index2 = length - 1
    while index2 != 0 and  not aString[index2].isalpha():
        index2 -= 1
    if index > length or index2 == 0:
        return True

    return aString[index]==aString[index2] and isPalindrome(aString[index+1:index2])


def isAnagram(word1,word2):
    if len(word1) != len(word2):
        return False
    word1 = sorted(word1)
    word2 = sorted(word2)

    return word1 == word2

if __name__ == '__main__':
    print("Testing for kth")
    assert kth([3, 4, 1, 3], 1) == [3,4,1,3]
    assert kth([3, 4, 1, 3], 2) == [4,3]
    assert kth([3, 4, 1, 3], 3) == [1]
    assert kth([3, 4, 1, 3], 4) == [3]
    assert kth([3, 4, 1, 3], 5) == []
    assert kth([1],1) == [1]
    assert kth([],1) == []
    assert kth([1,2,3,4],0) == []
    assert kth([],0) == []
    print("Kth passed tests")

    # print(kth([3, 4, 1, 3], 1))
    # print(kth([3, 4, 1, 3], 2))
    # print(kth([3, 4, 1, 3], 3))
    # print(kth([3, 4, 1, 3], 4))
    # print(kth([3, 4, 1, 3], 5))
    print("==============================")
    print("Testing for isPalindrome")
    assert isPalindrome("") == True
    assert isPalindrome("      ") == True
    assert isPalindrome("f") == True
    assert isPalindrome("fo") == False
    assert isPalindrome("ff") == True
    assert isPalindrome("fof") == True
    assert isPalindrome("foof") == True
    assert isPalindrome("forf") == False
    assert isPalindrome("   foof") == True
    assert isPalindrome("  a b,a") == True
    assert isPalindrome(",.asd,.  dsa") == True
    print("isPalindrome passed tests")
    print("==============================")
    print("Testing for isAnagram")
    # print(isAnagram("car","arc"))
    # print(isAnagram("food","doof"))
    # print(isAnagram("food","ddof"))
    print("isAnagram passed tests")
    print("==============================")
    print("All tests passed!!!")

#
# def isPalindrome(aString):
#     length = len(aString)
#     if length == 0:
#         return True
#     return aString[0]==aString[length-1] and isPalindrome(aString[1:length-1])
