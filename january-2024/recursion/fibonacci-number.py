#https://leetcode.com/problems/fibonacci-number/
class Solution:
    memo = {}

    def helper(self, n):
        if n in self.memo.keys():
            return self.memo[n]
        else:
            self.memo[n] = self.fib(n) # <-- recursion
            return self.memo[n]

    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.helper(n-1) + self.helper(n-2)

n = 7
s = Solution()
res = s.fib(n)

print(f"answer = {res}")
