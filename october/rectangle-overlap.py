# You are given 2 lists of coordinates in the format of [x1, y1, x2, y2]
# (x1, y1) is the coordinate of its bottom-left corner
# (x2, y2) is the coordinate of its top-right corner
# Two rectangles overlap if the area of their intersection is positive.
# To be clear, two rectangles that only touch at the corner or edges do not overlap.

# take a look at this example: https://leetcode.com/problems/rectangle-overlap/solutions/849096/solution-with-example-diagrams/
# class Solution:
#     def isRectangleOverlap(self, r1: List[int], r2: List[int]) -> bool:
#         x = sorted([(r1[0], "r1"), (r1[2], "r1"), (r2[0], "r2"), (r2[2], "r2")])
#         y = sorted([(r1[1], "r1"), (r1[3], "r1"), (r2[1], "r2"), (r2[3], "r2")])
        
#         if x[0][1] == x[1][1] or x[2][1] == x[3][1] or y[0][1] == y[1][1] or y[2][1] == y[3][1] or x[2][0] == x[1][0] or y[2][0] == y[1][0]:
#             return False
#         return True


# https://leetcode.com/problems/rectangle-overlap/solutions/639586/ac-simply-readable-python-one-line/
class Solution:
    def isRectangleOverlap(self, rec1, rec2):

        length, width = False, False

        x = max(rec1[0], rec2[0])
        y = min(rec1[2], rec2[2])
        if x < y:
            length = True

        p = max(rec1[1], rec2[1])
        q = min(rec1[3], rec2[3])
        if p < q:
            width = True

        return length and width


#[x1, y1, x2, y2]
# rec1 = [0,0,2,2]
# rec2 = [1,1,3,3]
#Output: true

# rec1 = [0,0,1,1]
# rec2 = [1,0,2,1]
#Output: false

rec1 = [7,8,13,15]
rec2 = [10,8,12,20]
#Output: true

s = Solution()
# print("## rec 1 ##")
# s.get_coords(rec1)
# print("## rec 2 ##")
# s.get_coords(rec2)



ans = s.isRectangleOverlap(rec1, rec2)

print(f"Answer = {ans}")
