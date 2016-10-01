def main():
    print(dispensingCash(12391))

def dispensingCash(amount):
    num100 = amount // 100
    amount %= 100
    num50 = amount // 50
    amount %= 50
    num20 = amount // 20
    amount %= 20
    num10 = amount // 10
    amount %= 10
    num5 = amount // 5
    amount %= 5
    num2 = amount // 2
    num1 = amount % 2
    return [num100,num50,num20,num10,num5,num2,num1]

main()