# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse_linked_list(head):
    prev = None
    curr = head
    while(curr):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        length = 0
        max_sum = 0

        curr = head
        while(curr):
            length += 1
            curr = curr.next
        
        half = head
        print(length)
        for i in range(length//2 -1):
            half = half.next

        second_half = half.next
        half.next = None
        curr2 = reverse_linked_list(second_half)
        curr1 = head

        while(curr1 and curr2):
            max_sum = max(max_sum, curr1.val + curr2.val)
            curr1, curr2 = curr1.next, curr2.next
        
        return max_sum