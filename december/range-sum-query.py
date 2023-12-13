#https://leetcode.com/problems/range-sum-query-immutable/description/
class NumArray:
    def __init__(self, nums):
        self.sum_dict = {}
        i = 0
        while i < len(nums):
            if i == 0:
                self.sum_dict[i] = nums[i]
            else:
                self.sum_dict[i] = nums[i]+self.sum_dict[i-1]
            i+=1

    def sumRange(self, left: int, right: int):
      return self.sum_dict[left] - self.sum_dict[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

nums = [-2, 0, 3, -5, 2, -1]
params = [[0, 2], [2, 5], [0, 5]]
NA = NumArray(nums)
for sub_arr in params:
    ans = NA.sumRange(sub_arr[0], sub_arr[1])
    print(ans)

# Expected Output
# [1,-1,-3]
# getting
# -4 -1 -4

#   0  1  2   3  4   5
# [-2, 0, 3, -5, 2, -1]
#  -2 -2  1  -4 -2  -3

# nums_dict = {}
