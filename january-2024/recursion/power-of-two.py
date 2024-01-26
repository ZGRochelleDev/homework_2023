#https://leetcode.com/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        elif n%2 != 0 or n < 1:
            return False
        return self.isPowerOfTwo(n/2)

n = 3
s = Solution()
res = s.isPowerOfTwo(n)

print(f"Result -> {res}")
