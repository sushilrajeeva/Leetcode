# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def getTail(self, lis: ListNode) -> ListNode:
        if not lis or lis.next is None:
            return lis
        
        cur: ListNode = lis
        prev: ListNode = None
        while cur:
            prev = cur
            cur = cur.next
        
        return prev
        

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        beforeA: ListNode = None
        afterB: ListNode = None
        current: ListNode = list1
        for i in range(b+2):
            if i == a-1:
                beforeA = current
            elif i == b+1:
                afterB = current
            current = current.next
        
        if beforeA:
            beforeA.next = list2
        
        tail: ListNode = self.getTail(list2)
        if afterB:
            tail.next = afterB

        return list1



        