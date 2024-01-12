# Write a recursive function to print all strings of length N
# that consist only of characters 'A' and 'B'
# class Solution:

# size = 2
# s = Solution()
# ans = s.permute(size)
# print(f"Solution -> {ans}")

# For input 2, Output will be
# AA
# AB
# BA
# BB

# For Input 3 as input
# AAA
# AAB
# ABA
# ABB
# BAA
# BAB
# BBA
# BBB

## iterative ##
def permute(arr):
    for x in range(len(arr)):
        return arr[x]

def permute_iterative(size):
    arr = ["A","B"]
    s1, s2 = "", ""

    # result = ""
    # for each in range(size):
    #     result = result + permute(arr)
    # print(result)

    for x in range(len(arr)):
        s1 = arr[x]
        for y in range(len(arr)):
            s2 = arr[y]
            for z in range(len(arr)):
                s3 = arr[z]
                print(s1+s2+s3)

    permute_arr = ["A" for x in range(size)] # list comprehension
    x = len(permute_arr)-1
    while x >= 0:
        permute_arr[x] = "B"
        x-=1
        print(permute_arr)

size = 3
print("iterative")
permute_iterative(size)


## recursive ##
def foo(build_array, letter, size):
    original_list = [build_array for x in range(size)]
    print(f"original_list: {original_list}")
    ptr = 0
    while ptr < len(original_list):
        print(original_list)
        ptr+=1
        original_list = [build_array for x in range(size)]
print("recursive")
size = 3
foo("A", "B", size)
foo("B", "A", size)
