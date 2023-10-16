# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#       count = 0
#       for jewel in jewels:
#         for stone in stones:
#           if jewel == stone:
#             count+=1
#       return count

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      s_dict = {}
      for stone in stones:
        if stone in s_dict.keys():
          s_dict[stone] = s_dict[stone] + 1
        else:
          s_dict[stone] = 1

      count = 0
      for jewel in jewels:
        try:
          count = count + s_dict[jewel]
        except:
          continue
        # if jewel in s_dict.keys():
        #   count = count + s_dict[jewel]
      return count

