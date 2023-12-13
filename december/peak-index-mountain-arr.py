#https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/
class Solution:
    def peakIndexInMountainArray(self, arr):
        # solve in O(log(n)) time

        ## attempt 1 ##
        # return arr.index(max(arr))

        ## attempt 2 ##
        # find i, where arr[i-1] < arr[i] > arr[i+1]
        i = 1
        while i < len(arr)-1:
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                return i
            else:
                i+=1

arr = [3,4,5,1]
#arr = [0,2,1,0]
#arr = [0,1,0]
s = Solution()
ans = s.peakIndexInMountainArray(arr)
print(f"peakIndexInMountainArray -> {ans}")
