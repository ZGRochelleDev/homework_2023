#https://leetcode.com/problems/palindromic-substrings/description/

class Solution:

    # def countSubstrings_2(self, s):
    #     substrings_count = 0
    #     str_size = len(s)
    #     for i in range(str_size):
    #         for a, b in [(i, i), (i, i+1)]:
    #             while a >= 0 and b < str_size and s[a] == s[b]:
    #                 a -= 1
    #                 b += 1
    #             substrings_count += (b-a)//2
    #     return substrings_count

    def countSubstrings_2(self, s):
        #base
        if i == str_size:
            return 0

#str = "aaaa"
str = "abba"
s = Solution()
ans = s.countSubstrings_2(str)

print("palindromic-substrings")
print(f"answer -> {ans}")
