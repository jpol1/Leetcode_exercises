# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None or k == 0:
            return head

        length = 0
        tail = head
        while (tail.next):
            length += 1
            tail = tail.next
        
        length += 1
        tail.next = head

        new_tail = head

        for i in range(length - (k % length) - 1):
            new_tail = new_tail.next

        head = new_tail.next
        new_tail.next = None

        return head