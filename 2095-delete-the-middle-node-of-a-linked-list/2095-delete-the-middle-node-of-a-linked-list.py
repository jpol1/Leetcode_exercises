# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
            
        curr = head
        length = 0
        while(curr):
            length +=1
            curr = curr.next
        
        mid = length // 2

        prev = None
        curr = head
        for i in range(mid):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        return head