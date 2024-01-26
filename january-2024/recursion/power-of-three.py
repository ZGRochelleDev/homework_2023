#https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        elif n%3 != 0 or n < 1:
            return False
        return self.isPowerOfThree(n/3)

n = 27
s = Solution()
res = s.isPowerOfThree(n)

print(f"Result -> {res}")
