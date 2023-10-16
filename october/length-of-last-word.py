## from the end ##
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      ## setting bound: getting the end char
      index = len(s)-1
      while(index >=0 and s[index] == " "):
        index-=1

      maxLength = 0
      ## counting the chars
      while(index >=0 and s[index] != " "):
        maxLength+=1
        index-=1
      return maxLength

## from the begining ##
# class Solution:
#     def compare(self, pre_ptr, post_ptr):
#       if pre_ptr > post_ptr:
#         temp = post_ptr
#         post_ptr = pre_ptr
#         pre_ptr = temp
#       return pre_ptr, post_ptr

#     def lengthOfLastWord(self, s: str) -> int:
#         size = len(s)
#         pre_ptr = 0
#         post_ptr = 0
#         for i in range(size):
#           if s[i] == " " or i == size-1:
#             if s[i-1] != " ":
#               pre_ptr = i
#               pre_ptr, post_ptr = self.compare(pre_ptr, post_ptr)
#             if i == size-1:
#               post_ptr = i
#         count = 0
#         for ea in s[pre_ptr:post_ptr+1]:
#           if ea != " ":
#             count+=1
#         return count
