# Write a recursive function to calculate the sum of the array
class Solution:

    def sum_array(self, array, i):
        # base case
        if i == len(arr):
            return 0
        # recursive case
        else:
            return self.sum_array(array, i+1) + array[i]

arr = [2,3,4,1,5,6,8] #10
print(f"Correct answer -> {sum(arr)}")
s = Solution()
ans = s.sum_array(arr, 0)
print(f"Solution -> {ans}")
