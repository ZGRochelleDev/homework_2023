## difficult to find efficient solution

#https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/
class Solution:
    def peakIndexInMountainArray(self, arr):
        # solve in O(log(n)) time

        ## attempt 1 O(n) ##
        # max_ptr = 0
        # for cur_ptr, num in enumerate(arr):
        #     if num > arr[max_ptr]:
        #         max_ptr = cur_ptr
        # return max_ptr

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


class Solution:

    def binary_iter(self, arr):

        return

    ## implement this from scratch
    def binary(self, left, right, arr):
        mid = int((left + right) / 2)
        if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid-1] < arr[mid]:
            return self.binary(mid + 1, right, arr)
        else:
            return self.binary(left, mid, arr)

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # i = 1
        # while i < len(arr)-1:
        #     if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
        #         return i
        #     else:
        #         i+=1

        return self.binary(0, len(arr)-1, arr)
