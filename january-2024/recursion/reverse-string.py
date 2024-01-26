#https://leetcode.com/problems/reverse-string/
class Solution:
    def helper(self, s, left, right):
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            return self.helper(s, left+1, right-1)

    def reverseString(self, s):
        self.helper(s, 0, len(s)-1)

n = ["h","e","l","l","o"]
s = Solution()

print(f"before -> {n}")
s.reverseString(n)
print(f"after -> {n}")
