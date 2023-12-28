#https://leetcode.com/problems/palindromic-substrings/description/

class Solution:

    def countSubstrings(self, s):
        no_of_substrings = 0

        x = 0
        while x < len(s):
            y = x+1
            while y <= len(s):
                substring = s[x:y]
                if substring == substring[::-1]:
                    no_of_substrings+=1
                y+=1
            x+=1
        
        return no_of_substrings

str = "abc"
#str = "aba"
s = Solution()
ans = s.countSubstrings(str)
print("palindromic-substrings")
print(f"answer -> {ans}")

