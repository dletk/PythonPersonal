def kth(L, k):
    """
    A recursive function to return a list including the k-1,2k-1,3k-1 (index).... element of original list

    :param L: the original list
    :param k: the number to use for incrementing
    :return: a list containing [L[k-1], L[2k-1], L[3k-1],...]
    """
    if len(L) == 0 or k == 0:
        return []
    return L[k-1:k]+(kth(L[k:], k))


def isPalindrome(aString):
    """
    A recursive function to test whether a string is a palindrome.
    Only consider alphabetical characters, strip out punctuations or white spaces.

    :param aString: the string to check whether it is a palindrome
    :return: True if the string is palindrome, otherwise False.
    """
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
    """
    Function to check whether 2 single word string are anagram.
    Take into account any character in ASCII table.

    :param word1: the first single word string
    :param word2: the second single word string
    :return: True if 2 strings are anagram, False otherwise.
    """
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
    assert isPalindrome("   a     ba  b") == False
    print("isPalindrome passed tests")
    print("==============================")
    print("Testing for isAnagram")
    assert isAnagram("","") == True
    assert isAnagram("car", "arc") == True
    assert isAnagram("food", "doof") == True
    assert isAnagram("food", "ddof") == False
    assert isAnagram("food12345", "43215dofo") == True
    assert isAnagram("12345abc", "2345abc") == False
    print("isAnagram passed tests")
    print("==============================")
    print("All tests passed!!!")

#
# def isPalindrome(aString):
#     length = len(aString)
#     if length == 0:
#         return True
#     return aString[0]==aString[length-1] and isPalindrome(aString[1:length-1])
