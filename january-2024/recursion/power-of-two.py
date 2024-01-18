#https://leetcode.com/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        if n%2 != 0 or n < 1:
            return False
        return self.isPowerOfTwo(n/2)

        # if n%2 == 0:
        #     return True
        # return False

n = 3
s = Solution()
res = s.isPowerOfTwo(n)

print(f"answer = {res}")
