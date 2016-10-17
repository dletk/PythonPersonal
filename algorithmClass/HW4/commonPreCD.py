def commonPreDC(aList):
    length = len(aList)
    if length == 1:
        return aList[0]
    else:
        long1 = commonPreDC(aList[:length//2])
        long2 = commonPreDC(aList[length//2:])
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
    assert commonPreDC(["absent", "abolish"]) == "ab"
    assert commonPreDC(["absent", "abolish", "apple"]) == "a"
    assert commonPreDC(["abcd123", "abc4d567", "abcdef", "abcd123"]) == "abc"
    assert commonPreDC(["abcdef"]) == "abcdef"
    assert commonPreDC(["abcdef", "defbca"]) == ""
    print("All tests passed!!!")
