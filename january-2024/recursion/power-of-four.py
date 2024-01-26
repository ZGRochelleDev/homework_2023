#https://leetcode.com/problems/power-of-four/
class Solution:
    def isPowerOfFour(self, n):
        if n == 1:
            return True
        elif n%4 != 0 or n < 1:
            return False
        return self.isPowerOfFour(n/4)

n = 16
s = Solution()
res = s.isPowerOfFour(n)

print(f"Result -> {res}")
