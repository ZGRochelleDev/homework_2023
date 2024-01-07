## binary_search ##
# https://www.geeksforgeeks.org/python-program-for-binary-search/

def binary_search(arr, low, high, target):
    # base case
    if low <= high:
        mid = (low + high) // 2 # floor division, rounds down
        # if the element is present at the middle
        if arr[mid] == target:
            return mid
        # if element is smaller than mid, then it must be present in left subarray
        elif target < arr[mid]:
            return binary_search(arr, low, mid-1, target)
        # else, the element can only be present in right subarray
        else:
            return binary_search(arr, mid+1, high, target)
    else:
        # the element is not present in the array
        return -1

# array must be in order
arr = [1,3,4,6,7,8,9,11,13,15,20,22]
int_to_find = 15
ans = binary_search(arr, 0, len(arr)-1, int_to_find)
print(f"solution -> {ans}, number {arr[ans]}")

# it's really just a couple of lines
# def binary_search(arr, left, right, target):
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     if target < arr[mid]:
#         return bs(arr, left, mid-1, target)
#     else:
#         return bs(arr, mid+1, right, target)