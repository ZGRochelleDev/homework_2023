# class Solution:
#     def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

#         bot_l_corner_1 = (rec1[0], rec1[1])
#         up_r_corner_1 = (rec1[2], rec1[3])

#         bot_l_corner_2 = (rec2[0], rec2[1])
#         up_r_corner_2 = (rec2[2], rec2[3])

#         if bot_l_corner_1 < up_r_corner_2 and bot_l_corner_1 > bot_l_corner_2:
#             print("check 1")

#             length = rec1[0] - rec2[2]
#             width = rec2[3] - rec1[1]

#             if length * width > 0:
#                 return True
#             else:
#                 return False

#         elif (bot_l_corner_2 < up_r_corner_1) and (bot_l_corner_2 > bot_l_corner_1):
            
#             length = rec2[0] - rec1[2]
#             width = rec1[3] - rec2[1]

#             print("check 2", length, width)

#             if length * width > 0:
#                 return True
#             else:
#                 return False
#         else:
#             print("neither conditions")
#             return False

# class Solution:
#     def __init__(self):
#         self.x_bounds = 0
#         self.y_bounds = 0

#     def determine_bounds(self, rec1, rec2):
#         x_upper = min(max(rec1[0], rec1[2]), max(rec2[0], rec2[2]))
#         y_upper = min(max(rec1[1], rec1[3]), max(rec2[1], rec2[3]))

#         x_lower = min(min(rec1[0], rec1[2]), min(rec2[0], rec2[2]))
#         y_lower = min(min(rec1[1], rec1[3]), min(rec2[1], rec2[3]))

#         return [x_lower, x_upper], [y_lower, y_upper]

#     def x_within_bounds(self, val):
#         if val >= self.x_bounds[0] and val <= self.x_bounds[1]:
#             return True
#         else:
#             return False

#     def y_within_bounds(self, val):
#         if val >= self.y_bounds[0] and val <= self.y_bounds[1]:
#             return True
#         else:
#             return False

#     def permute_tuples(self, rec):
#         arr = []
#         for x in range(rec[0], rec[2]+1):
#             for y in range(rec[1], rec[3]+1):
#                 if self.x_within_bounds(x) and self.y_within_bounds(y):
#                     arr.append((x,y))
#         return arr

#     def isRectangleOverlap(self, rec1, rec2):
#         self.x_bounds, self.y_bounds = self.determine_bounds(rec1, rec2)

#         rec1_tuples = self.permute_tuples(rec1)
#         rec2_tuples = self.permute_tuples(rec2)

#         tuples_sm = rec1_tuples if len(rec1_tuples) <= len(rec2_tuples) else rec2_tuples
#         tuples_lg = rec2_tuples if len(rec2_tuples) >= len(rec1_tuples) else rec1_tuples

#         s_arr = []
#         for ea in tuples_sm:
#             if ea in tuples_lg:
#                 s_arr.append(ea)

#         if len(s_arr) % 2 == 0:
#             return True
#         else:
#             return False

# class Solution:
#     def permute_tuples(self, rec):
#         arr = []
#         for x in range(rec[0], rec[2]):
#             for y in range(rec[1], rec[3]):
#                 arr.append((x,y))
#         return arr

#     def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

#         rec1_tuples = self.permute_tuples(rec1)
#         rec2_tuples = self.permute_tuples(rec2)

#         overlap_arr_1 = []
#         overlap_arr_2 = []
#         for rec1_tuple in rec1_tuples:
#             if rec1_tuple in rec2_tuples and max(rec2) not in rec1_tuple and min(rec2) not in rec1_tuple:
#                 overlap_arr_1.append(rec1_tuple)

#         for rec2_tuple in rec2_tuples:
#             if rec2_tuple in rec1_tuples and max(rec1) not in rec2_tuple and min(rec1) not in rec2_tuple:
#                 overlap_arr_2.append(rec2_tuple)

#         if overlap_arr_1 == overlap_arr_2:
#             return False
#         else:
#             return True
