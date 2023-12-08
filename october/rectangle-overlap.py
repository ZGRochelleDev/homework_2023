# You are given 2 lists of coordinates in the format of [x1, y1, x2, y2]
# (x1, y1) is the coordinate of its bottom-left corner
# (x2, y2) is the coordinate of its top-right corner
# Two rectangles overlap if the area of their intersection is positive.
# To be clear, two rectangles that only touch at the corner or edges do not overlap.

# whether the points are bottom-left or top-right matters for the solution.
# for example, you could not treat a bottom-left corner as a bottom-right.

class Solution:
    def isRectangleOverlap(self, rec1, rec2):

        length, width = False, False

        # (x1, y1) = bottom-left
        # (x2, y2) = top-right

        # compare the bounds of
        # then left to right
        # bottom to top
        
        # left to right
        # left must be less than right
        # think about it's position on a graph
        x1 = max(rec1[0], rec2[0]) # left
        x2 = min(rec1[2], rec2[2]) # right

        if x1 < x2:
            length = True

        # bottom to top
        # bottom must be less than top
        y1 = max(rec1[1], rec2[1]) # bottom
        y2 = min(rec1[3], rec2[3]) # top

        if y1 < y2:
            width = True

        return length and width
        
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
s = Solution()
ans = s.isRectangleOverlap(rec1, rec2)
print(ans)


