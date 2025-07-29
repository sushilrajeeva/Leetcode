# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNodeLength(self, head: Optional[ListNode]) -> int:
        length = 0
        current: Optional[ListNode] = head
        while current:
            length += 1
            current = current.next
        return length

    def getToDelNode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 0
        current: Optional[ListNode] = head
        while current:
            if i == k:
                return current
            i += 1
            current = current.next
        return current
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length: int = self.getNodeLength(head)
        k = length - n
        to_del: Optional[ListNode] = self.getToDelNode(head, k)
        if not to_del:
            return head
        current: Optional[ListNode] = head
        prev: Optional[ListNode] = None
        while current:
            next = current.next
            if current == to_del:
                current.next = None
                if prev:
                    prev.next = next
                    return head
                else:
                    return next
            else:
                prev = current
                current = current.next
        return head
                


        
        