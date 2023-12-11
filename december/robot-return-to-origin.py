class Solution:
    def judgeCircle(self, moves):
        u = moves.count('U')
        d = moves.count('D')
        l = moves.count('L')
        r = moves.count('R')

        return u == d and l == r
        
        
        


# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         moves_dict = {
#             "U":[0,1],
#             "D":[0,-1],
#             "L":[-1,0],
#             "R":[1,0]
#             }

#         origin = [0,0]
#         cur_pos = origin

#         for move in moves:
#             md = moves_dict[move]
#             cur_pos = [cur_pos[0]-md[0], cur_pos[1]-md[1]]

#         return origin == cur_pos

moves = "ULDR"
s = Solution()
ans = s.judgeCircle(moves)
print(f"Answer -> {ans}")



# is there an equal number of L and R
# U and D