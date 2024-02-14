import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname('C:/Users/zogr2/Documents/GitHub/homework_2023/modules'))
from modules.linked_list import *

## iterative
# class Solution(object):
#     def isPalindrome(self, head):
#         l_list = []
#         node = head
#         while node is not None:
#             l_list.append(node.val)
#             node = node.next

#         if l_list == l_list[::-1]:
#             return True
#         else:
#             return False

## old recursion method
# class Solution(object):
#     pal_list = []
#     def helper(self, l, r):
#       if l > r:
#         return True
#       elif self.pal_list[l] != self.pal_list[r]:
#         return False

#       return self.helper(l+1, r-1)

#     def isPalindrome(self, head):
#       self.pal_list = []
#       while head:
#         self.pal_list.append(head.val)
#         head = head.next
#       return self.helper(0, len(self.pal_list)-1)

## new reursion method
class Solution(object):
    def isPalindrome(self, head):
        self.left = ListNode(0, head)

        def recursion(head):
            if not head:
                return True

            right = recursion(head.next)
            self.left = self.left.next
            return right and self.left.val == head.val
            # If any of the checks fails while returning, then we are sure that its not palindrome.
            # If not a palendrome, then he above return statement will always return false.
            # So, right is used to check whether the previously done checks are also True or not.

        return recursion(head)


#l1 = ListNode(1, ListNode(2, ListNode(4)))
LLC = LinkedListClass()


test_case = [1,2,3,2,1]
#test_case = [1,2,3]
linked_list_1 = LLC.create_linked_list(test_case)
LLC.print_linked_list(linked_list_1)

s = Solution()
res = s.isPalindrome(linked_list_1)

print(f"Answer -> {res}")
