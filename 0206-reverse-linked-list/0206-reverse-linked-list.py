# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current: Optional[ListNode] = head
        previous: Optional[ListNode] = None
        
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        
        return previous
    

        