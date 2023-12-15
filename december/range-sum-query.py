#https://leetcode.com/problems/range-sum-query-immutable/description/
## Attempt 2 ##
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
      if left == 0:
          return self.sum_dict[right]
      else:
        return self.sum_dict[right]-self.sum_dict[left-1]

## Attempt 1 ##
# class NumArray:
#     nums_list = []
#     arr_sum = []

#     def __init__(self, nums: List[int]):
#         self.nums_list = nums
#         ## add preprocessing here
#         ## to call in sumRange

#     def sumRange(self, left: int, right: int) -> int:
      
#       sum = 0
#       for pos in range(left, right+1):
#           sum = sum + self.nums_list[pos]
#       return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
#              2          5
nums = [-2, 0, 3, -5, 2, -1]
params = [[0, 2], [2, 5], [0, 5]]
NA = NumArray(nums)
print(NA.sum_dict.values())
ans = []
for sub_arr in params:
    ans.append(NA.sumRange(sub_arr[0], sub_arr[1]))
print(f"ans -> {ans}")

# Expected Output
# [1,-1,-3]
# getting
# -4 -1 -4

#   0  1  2   3  4   5
# [-2, 0, 3, -5, 2, -1]
#  -2 -2  1  -4 -2  -3



class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.sum_dict = nums # array better space?

        i = 0
        while i < len(nums):
            if i == 0:
                self.sum_dict[i] = nums[i]
            else:
                self.sum_dict[i] += self.sum_dict[i-1]
            i+=1

    def sumRange(self, left: int, right: int):
      if left == 0:
          return self.sum_dict[right]
      else:
        return self.sum_dict[right] - self.sum_dict[left-1]

# class NumArray:
#     nums_list = []
#     arr_sum = []

#     def __init__(self, nums: List[int]):
#         self.nums_list = nums
#         ## add preprocessing here
#         ## to call in sumRange

#     def sumRange(self, left: int, right: int) -> int:
      
#       sum = 0
#       for pos in range(left, right+1):
#           sum = sum + self.nums_list[pos]
#       return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
