if __name__ == '__main__':

    input_nums = input()
    print(input_nums)
    input_nums = input_nums.split()
    for i in range(len(input_nums)):
        print("Got number "+input_nums[i])