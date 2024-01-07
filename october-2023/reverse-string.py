class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        #s = s[::-1]
        # 2 ptr
        l = 0
        r = len(s)-1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1

        # try w/ 1 ptr <- O(1)*n/2    - more memory efficient



str_list = ["h","e","l","l","o"]
s = Solution()
ans = s.reverseString(str_list)

print(ans)


