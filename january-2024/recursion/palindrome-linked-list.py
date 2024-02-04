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
