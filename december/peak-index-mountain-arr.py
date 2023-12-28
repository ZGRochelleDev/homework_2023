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

class Solution:

    def binary_iter(self, l, h, arr):
        while l < h:
            mid = (l + h) // 2
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                h = mid
        return mid

    def binary(self, left, right, arr):
        mid = int((left + right) / 2)
        if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid-1] < arr[mid]:
            return self.binary(mid + 1, right, arr)
        else:
            return self.binary(left, mid, arr)

    def peakIndexInMountainArray(self, arr):
        #return self.binary(0, len(arr)-1, arr)
        return self.binary_iter(0, len(arr)-1, arr)

arr = [3,4,5,1]
#arr = [0,2,1,0]
#arr = [0,1,0]
s = Solution()
ans = s.peakIndexInMountainArray(arr)
print(f"peakIndexInMountainArray -> {ans}")

# def binary_iter(self, l, h, arr, target):
#     target = 1
#     mid = (l + h) // 2
#     while l < h:
#         if arr[mid] == target:
#             return mid
#         elif target < arr[mid]:
#             h = mid - 1
#             mid = (l + h) // 2
#         else:
#             l = mid + 1
#             mid = (l + h) // 2

def round_float(num):
    if num % 1 >= .5:
        return int(num + 1)
    else:
        return int(num)

## implement this from scratch
# def binary_search(left, right, arr, target):
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     if target < arr[mid]:
#         right = mid
#         return binary_search(left, right, arr, target)
#     elif arr[mid] > target:
#         left = mid
#         return binary_search(left, right, arr, target)
#     else:
#         return -1

# arr = [1,3,5,6,7,8,9,12,15]
# target = 5
# ans = binary_search(0,len(arr)-1, arr, 5)

# print(f"Answer -> {ans}")
