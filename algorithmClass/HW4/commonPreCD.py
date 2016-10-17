def longestPrefix(aList):
    length = len(aList)
    if length == 0:
        return ""
    elif length == 1:
        return aList[0]
    else:
        long1 = longestPrefix(aList[:length//2])
        long2 = longestPrefix(aList[length//2:])
        lenMin = min(len(long1),len(long2))
        i = 0
        result = ""
        while i<lenMin:
            if long1[i]==long2[i]:
                result += long1[i]
            else:
                break
            i += 1
        return result

if __name__ == '__main__':
    assert longestPrefix(["absent", "abolish"]) == "ab"
    assert longestPrefix(["absent", "abolish", "apple"]) == "a"
    assert longestPrefix(["abcd123", "abc4d567", "abcdef", "abcd123"]) == "abc"
    assert longestPrefix(["abcdef"]) == "abcdef"
    assert longestPrefix(["abcdef", "defbca"]) == ""
    assert longestPrefix([]) == ""
    assert longestPrefix(["","abcdef","abcdefa","abcdefac"]) == ""
    print("All tests passed!!!")
