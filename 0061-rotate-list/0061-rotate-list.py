# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLinkedListLength(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        x = 0
        while head:
            x += 1
            head = head.next
        return x

    def getLastNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur = head
        while cur.next:
            cur = cur.next
        return cur


    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        n = self.getLinkedListLength(head)
        k = k%n

        if k == 0: return head

        y = n - k - 1
        cur = head

        for i in range(y):
            cur = cur.next
        
        next = cur.next
        cur.next = None
        lastNode = self.getLastNode(next)
        lastNode.next = head
        return next


        