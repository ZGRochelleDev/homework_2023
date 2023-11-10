## from the end ##
print("## From the end ##")
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      ## setting bound: getting the end char
      index = len(s)-1
      while(index >=0 and s[index] == " "): # while not at the end of the array, and the char is a space, decrement --1. Basically: "find the first non space char, from the end of the array".
        index-=1

      maxLength = 0
      ## counting the chars
      while(index >=0 and s[index] != " "):
        maxLength+=1
        index-=1
      return maxLength

test_cases = [
  "  H ",
  "H",
  "Hello",
  "Hello World",
  "   fly me   to   the moon  ",
  "luffy is still joyboy"
]

s = Solution()
for ea in test_cases:
  print(f"Len of last word = {s.lengthOfLastWord(ea)}")

## from the beginning ##
print("## From the beginning ##")
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      ## setting bound: getting the first non space char
      index = 0
      ptr = index
      while(index < len(s)):
        # create a pointer to keep track of the 1st character in a word
        if s[index] != " " and s[index-1] == " ":
          #update the pointer
          ptr = index
        index+=1

      maxLength = 0
      ## counting the chars
      while(ptr < len(s) and s[ptr] != " "):
        maxLength+=1
        ptr+=1
      return maxLength

test_cases = [
  "  H ",
  "H",
  "Hello",
  "Hello World",
  "   fly me   to   the moon  ",
  "luffy is still joyboy"
]

s = Solution()
for ea in test_cases:
  print(f"Len of last word = {s.lengthOfLastWord(ea)}")
