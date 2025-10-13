# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # def getReverseLinkedListHead(self, node: ListNode) -> Optional[ListNode]:
    #     if not node or not node.next:
    #         return node
    #     prev = None
    #     current = node

    #     while current:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
        
    #     return prev



    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        A = []
        B = []

        curA = headA
        curB = headB

        while curA:
            A.append(curA)
            curA = curA.next
        while curB:
            B.append(curB)
            curB = curB.next

        n = len(A) - 1
        m = len(B) - 1

        if A[-1].val != B[-1].val: return None
        prev = None

        while n >= 0 and m >= 0:
            if A[n] != B[m]:
                return prev
            prev = A[n]
            n -= 1
            m -= 1

        return prev