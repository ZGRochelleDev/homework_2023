## binary_search ##
# https://www.geeksforgeeks.org/python-program-for-binary-search/

def binary_search(arr, low, high, x):
    # base case
    if low <= high:
        mid = (high + low) // 2 # floor division
        # if the element is present at the middle
        if arr[mid] == x:
            return mid
        # if element is smaller than mid, then it must be present in left subarray
        elif x < arr[mid]:
            return binary_search(arr, low, mid - 1, x)
        # else, the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # the element is not present in the array
        return -1

# array must be in order
arr = [1,6,8,10,15,22]
int_to_find = 6

res = binary_search(arr, 0, len(arr)-1, int_to_find)
print(f"Answer -> {res}")

## python rounds down - floor division ##
# x = 11/2
# y = 11//2
# z = int(11/2)
# print(x, y, z)
