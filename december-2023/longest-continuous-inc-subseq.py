#https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums):
        res = []
        i = 1
        count = 1

        if len(nums) <= 1:
            return len(nums)

        while i < len(nums):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                res.append(count)
                count = 1
            i+=1
        res.append(count)

        return max(res)




class Solution:
    def findLengthOfLCIS(self, nums):
        arr_size = len(nums)

        ## case where nums == 1 or 0
        if arr_size <= 1:
            return arr_size

        i = 1
        subseq_count = 1
        largest = 1
        while i < arr_size:
            if nums[i] > nums[i-1]:
                subseq_count += 1
            else:
                if subseq_count > largest:
                    largest = subseq_count # update the largest value
                subseq_count = 1
            i+=1

        # if the last loop incremented the count, then we need to check if it's greater
        if subseq_count > largest:
            largest = subseq_count

        return largest

nums = [1,3,5,4,2,3,4,5]
#nums = []
s = Solution()
ans = s.findLengthOfLCIS(nums)
print("longest-continuous-increasing-subsequence")
print(f"answer -> {ans}")


# can i use binary search to find all positions where nums[i-1] > nums[i]?



