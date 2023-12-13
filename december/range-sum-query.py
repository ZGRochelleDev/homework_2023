#https://leetcode.com/problems/range-sum-query-immutable/description/
class NumArray:
    nums_list = []
    arr_sum = []

    def __init__(self, nums: List[int]):
        self.nums_list = nums
        ## add preprocessing here
        ## to call in sumRange

    def sumRange(self, left: int, right: int) -> int:
      
      sum = 0
      for pos in range(left, right+1):
          sum = sum + self.nums_list[pos]
      return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
