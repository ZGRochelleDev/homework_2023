#https://leetcode.com/problems/palindromic-substrings/description/


# odd vs even?
# aaaaaaaa


class Solution:
    def countSubstrings(self, s):
        no_of_substrings = 0
        str_size = len(s)
        for i in range(str_size):

            for a, b in [(i,i), (i,i+1)]:
                while a >= 0 and b < str_size and s[a] == s[b]:
                    a -= 1
                    b += 1
                    no_of_substrings += (b-a)//2
        return no_of_substrings

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

    def countSubstrings_1(self, s):
        no_of_substrings = 0
        str_size = len(s)
        for i in range(str_size):
            no_of_substrings+=1
            iter = 1
            while i-iter >= 0 and i+iter < str_size:
                if s[i] == s[i+iter]:
                    no_of_substrings+=1
                elif s[i] == s[i-iter]:
                    no_of_substrings+=1
                iter+=1
        return no_of_substrings

    def countSubstrings_2(self, s):
        no_of_substrings = 0
        str_size = len(s)
        for i in range(str_size):
            for a, b in [(i, i), (i, i+1)]:
                print(a,b,"-",[(i, i), (i, i+1)])
                while a >= 0 and b < str_size and s[a] == s[b]:
                    a -= 1
                    b += 1
                no_of_substrings += (b-a)//2
        return no_of_substrings


str = "aa"
#str = "aba"
s = Solution()
ans = s.countSubstrings_2(str)
#ans = s.countSubstrings_1(str)
#ans = s.countSubstrings(str)
print("palindromic-substrings")
print(f"answer -> {ans}")

