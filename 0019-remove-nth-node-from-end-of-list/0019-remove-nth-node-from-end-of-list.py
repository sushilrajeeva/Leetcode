# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Dummy node points to head, so deleting head is uniform
        dummy = ListNode(0, head)
        
        first = dummy
        second = dummy
        
        # Move `first` n+1 steps ahead, so the gap between first and second is n nodes
        for _ in range(n + 1):
            first = first.next
        
        # Advance both until first hits the end
        while first:
            first = first.next
            second = second.next
        
        # Now second.next is the node to delete; unlink it
        second.next = second.next.next
        
        # Return the (possibly new) head
        return dummy.next