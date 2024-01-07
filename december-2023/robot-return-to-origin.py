#https://leetcode.com/problems/robot-return-to-origin/submissions/
class Solution:
    def judgeCircle(self, moves):
        ## Second attempt ##
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')  

        ## First attempt ##
        # moves_dict = {
        #     "U":[0,1],
        #     "D":[0,-1],
        #     "L":[-1,0],
        #     "R":[1,0]
        #     }

        # origin = [0,0]
        # cur_pos = origin

        # for move in moves:
        #     md = moves_dict[move]
        #     cur_pos = [cur_pos[0]-md[0], cur_pos[1]-md[1]]

        # return origin == cur_pos
