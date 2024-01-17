# memoization
# dfs
# every branch will always end in a 1 or a 2
#             4
#        /         \
#      2            3
#    /     \       /    \
#    1    0      2      1
#  /           /   \      \ 
# 0           1     0       0
#           /
#         0


## better time complexity - source: https://leetcode.com/problems/climbing-stairs/solutions/1671910/python-detailed-explanation-o-n-time-o-n-space-beats-92-05-time/
class Solution:
    def climbStairs(self, n, memo = {1:1, 2:2}):
        if n in memo.keys():
            return memo[n]
        memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n]

## my original solution ##
# class Solution:
#     memo = {}
#     def climbStairs(self, n):
#         if n == 0:
#             return 1
#         if n < 0:
#             return 0

#         if n-1 in self.memo.keys():
#             val1 = self.memo[n-1]
#         else:
#             val1 = self.climbStairs(n-1)
#             self.memo[n-1] = val1

#         if n-2 in self.memo.keys():
#             val2 = self.memo[n-2]
#         else:
#             val2 = self.climbStairs(n-2)
#             self.memo[n-2] = val2

#         return val1 + val2


n = 5
s = Solution()
res = s.climbStairs(n)

print(f"Result -> {res}")
