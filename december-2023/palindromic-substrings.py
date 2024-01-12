#https://leetcode.com/problems/palindromic-substrings/description/


# odd vs even?
# aaaaaaaa

class Solution:

    ## first attempt - traversing left to right
    def countSubstrings(self, s):
        substrings_count = 0
        x = 0
        while x < len(s):
            y = x+1
            while y <= len(s):
                substring = s[x:y]
                if substring == substring[::-1]:
                    substrings_count+=1
                y+=1
            x+=1
        return substrings_count

    ## second attempt - traversing middle out
    # write code for odd
    # write code for even
    # see simlarities -> redundancies
    # write a consolidated version
    def countSubstrings_1(self, s):
        substrings_count = 0
        str_size = len(s)
        for i in range(str_size):
            substrings_count+=1
            iter = 1
            while i-iter >= 0 and i+iter < str_size:
                if s[i] == s[i+iter]: # manam  i=2
                    # while iter =0 -> (i-iter>=0) (i + iter < len)
                    substrings_count+=1
                elif s[i] == s[i-iter]:
                    substrings_count+=1
                iter+=1
        return substrings_count

    ## third attempt - traversing middle out (had to look this up)
    def countSubstrings_2(self, s):
        substrings_count = 0
        str_size = len(s)
        for i in range(str_size):
            for a, b in [(i, i), (i, i+1)]:
                #print(a,b,"-",[(i, i), (i, i+1)])
                while a >= 0 and b < str_size and s[a] == s[b]:
                    print(f"a: {s[a]}, {a}, b: {s[b]}, {b}")
                    a -= 1
                    b += 1
                substrings_count += (b-a)//2
        return substrings_count


#str = "aa"
str = "aba"
s = Solution()
ans = s.countSubstrings_2(str)
#ans = s.countSubstrings_1(str)
#ans = s.countSubstrings(str)
print("palindromic-substrings")
print(f"answer -> {ans}")
