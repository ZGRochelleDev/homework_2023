# Write a recursive function to print all strings of length N
# that consist only of characters 'A' and 'B'
# class Solution:

#     def permute(self, size):
#         return

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
arr = ["A","B"]
s1, s2 = "", ""

for x in range(2):
    s1 = arr[x]
    for y in range(2):
        s2 = arr[y]
        print(s1+s2)

size = 3
permute_arr = ["A" for x in range(size)] # list comprehension
x = len(permute_arr)-1
while x >= 0:
    permute_arr[x] = "B"
    x-=1
    print(permute_arr)

def foo(build_array, letter, size):
    original_list = [build_array for x in range(size)]
    print(original_list)
    ptr = 0
    while ptr < len(original_list):


        print(original_list)
        ptr+=1
        original_list = [build_array for x in range(size)]
size = 3
foo("A", "B", size)
foo("B", "A", size)
