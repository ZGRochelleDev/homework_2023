## Method 1 ##
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#       count = 0
#       for jewel in jewels:
#         for stone in stones:
#           if jewel == stone:
#             count+=1
#       return count

## Method 2 ##
# class Solution:
#     def numJewelsInStones(self, jewels, stones) -> int:
#       s_dict = {}
#       for stone in stones:
#         if stone in s_dict.keys():
#           s_dict[stone] = s_dict[stone] + 1
#         else:
#           s_dict[stone] = 1

#       count = 0
#       for jewel in jewels:
#         try:
#           count = count + s_dict[jewel]
#         except:
#           continue

#       return count

## Method 3 ##
class Solution:
    def numJewelsInStones(self, jewels, stones) -> int:

      mapping_dict = {}
      # using a dictionary for mapping instead of an array.
      # ord() returns an int representing a Unicode character.

      for j in jewels:
        #lowercase
        if j >= "a" and j <= "z":
          mapping_dict[ord(j) - ord('a')] = 1
        #capital letter
        elif j >= "A" and j <= "Z":
          mapping_dict[ord(j) - ord('A') + 26] = 1

      count = 0
      for s in stones:
        if s >= "a" and s <= "z":
          key = ord(s) - ord('a')
          if key in mapping_dict: # <- first check if key exists in the dictionary
            if mapping_dict[key] > 0:
              count+=1

        elif s >= "A" and s <= "Z":
          key = ord(s) - ord('A') + 26
          if key in mapping_dict: # <- first check if key exists in the dictionary
            if mapping_dict[key] > 0:
              count+=1

      return count


jewels = "aA"
stones = "aAAbbbb"

s = Solution()
ans = s.numJewelsInStones(jewels, stones)

print(f"Answer = {ans}")


## simpler, but less efficient method ##
# class Solution:
#     def numJewelsInStones(self, jewels, stones):
#         count = 0
#         for stone in stones:
#             for jewel in jewels:
#                 if jewel == stone:
#                     count+=1
#         return count


