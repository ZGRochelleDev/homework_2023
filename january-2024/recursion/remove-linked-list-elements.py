import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname('C:/Users/zogr2/Documents/GitHub/homework_2023/modules'))
from modules.linked_list import *

class Solution:
    def removeElements(self, head, val):
        # base case
        if head is None:
          return head

        # recursive case - this becomes w/e the return value is below
        head.next = self.removeElements(head.next, val)

        # we can define what the return val is here. Consider that the result of the assignment above has not yet been determined.

        # below is where the removal is performed
        if head.val == val:
          head = head.next

        # this return value will result from either the assignment above or unchanged
        return head
    
test_case = [1,2,6,3,4,5,6]
LLC = LinkedListClass()
linked_list_1 = LLC.create_linked_list(test_case)

#LLC.print_linked_list(linked_list_1)

s = Solution()
res = s.removeElements(linked_list_1, 6)




print(f"result -> {res}")
LLC.print_linked_list(res)



