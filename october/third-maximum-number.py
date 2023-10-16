## Using Sorting
class Solution:

    def de_duplicate(self, nums):
        new_nums = []
        s = sorted(nums, reverse=True)
        smallest = s[0]
        new_nums.append(smallest)
        for each in s:
            if each < smallest:
                new_nums.append(each)
                smallest = each
        return new_nums

    def thirdMax(self, nums):
        if len(nums) > 2:
            nums_de_dup = self.de_duplicate(nums)
            if len(nums_de_dup) >= 3:
                return nums_de_dup[2]

        return max(nums)

# class Solution:

#     def swap_check(self, x, y):
#         if x > y:
#             return True
#         else:
#             return False

#     def thirdMax(self, nums):

#         if len(nums) == 3:
#             if nums[0] != nums[1] != nums[2]:
#                 s_nums = sorted(nums)
#                 return s_nums[0]
#             else:
#                 return max(nums)
#         print(len(nums))
#         if len(nums) > 3:


#             first = 0
#             second = 0
#             third = 0

#             i = 0
#             while i < len(nums):
#                 if nums[i] > first:
#                     if self.swap_check(first, second):
#                         second = first
#                     first = nums[i]

#                 elif nums[i] > second:
#                     if self.swap_check(second, third):
#                         third = second
#                     second = nums[i]

#                 elif nums[i] > third:
#                     third = nums[i]
#                 i+=1
#             return third
#         else:
#             print("here")
#             return max(nums)


