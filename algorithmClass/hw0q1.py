def main():
    print(secondLargest([-10,-9,-8,-7,-6,-5,0]))
    print(secondLargest([5,2,6,8,3,11,7,9,4,0]))
    print(secondLargest([1,2,3,4,5,6,7,8,9,10,11]))
    print(secondLargest([20,19,18,17,16,15,14,13,12,11,10]))

def secondLargest(a):
    largest = a[0]
    secondLargest = 0
    for i in range(2,len(a),1):
        if a[i] > largest:
            secondLargest = largest
            largest = a[i]
        elif a[i] > secondLargest:
            secondLargest = a[i]
    return secondLargest

main()

