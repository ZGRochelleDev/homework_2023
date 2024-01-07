class Solution:
    def pos_check(self, f, s, t):
        return sorted([f,s,t])[::-1]

    def thirdMax(self, nums):
        set_nums = set(nums) # de-duplicate, otherwise we can't initialize first, second, third variables in the case of arr = [2,2,3,1]
        lst_nums = list(set_nums)

        if len(lst_nums) < 3:
            return max(lst_nums)

        f = lst_nums[0]
        s = lst_nums[1]
        t = lst_nums[2]

        f, s, t = self.pos_check(f,s,t)

        for num in lst_nums:
            if num > t and num != s and num != f:
                t = num
                f, s, t = self.pos_check(f,s,t)
        return t

# class Solution:
    def swap(self, f, s, t): # 1 4 5
      # make this a nested if
      # only need to check the 3rd largest
      # only update if n>
      if f < s:
        tmp = f
        f = s
        s = tmp
      if f < t:
        tmp = f
        f = t
        t = tmp
      if s < t:
        tmp = s
        s = t
        t = tmp
      return f,s,t

#     def thirdMax(self, nums):

#       nums = list(set(nums)) # de-duplicate, otherwise we can't initialize first, second, third variables in the case of arr = [2,2,3,1]

#       if len(nums)>2:
#         first, second, third = self.swap(nums[0], nums[1], nums[2])
#         for num in nums[2:]:
#           if num > third:
#             if num != second and num != first:
#               third = num
#               first, second, third = self.swap(first, second, third)
#       else:
#         third = max(nums)
#       return third

arr = [1,2,2,5,3,5]
s = Solution()
print(f"Arr = {arr}")
print(f"Third Max = {s.thirdMax(arr)}")

## Using Sorting ##
# class Solution:
#     def de_duplicate(self, nums):
#         new_nums = []
#         s = sorted(nums, reverse=True)
#         smallest = s[0]
#         new_nums.append(smallest)
#         for each in s:
#             if each < smallest:
#                 new_nums.append(each)
#                 smallest = each
#         return new_nums

#     def thirdMax(self, nums):
#         if len(nums) > 2:
#             nums_de_dup = self.de_duplicate(nums)
#             if len(nums_de_dup) >= 3:
#                 return nums_de_dup[2]

#         return max(nums)
