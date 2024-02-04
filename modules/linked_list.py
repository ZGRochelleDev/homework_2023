class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListClass:

    def insert(self, head, data):
        if (head == None):
            head = ListNode(data)
        else:
            current = head ## assign the pointer to current
            while (current.next != None):
                current = current.next
            current.next = ListNode(data)
        return head

    def print_linked_list(self, head):
        while head != None:
            print(head.val)
            head = head.next

    ## create a new linked list
    def create_linked_list(self, val_arr):
        l_list = ListNode(0)
        for val in val_arr:
            l_list = self.insert(l_list, val)
        return l_list.next
