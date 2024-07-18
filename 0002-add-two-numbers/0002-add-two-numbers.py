# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2

        dummy = ListNode(-1)
        current = dummy
        carry = 0

        while cur1 and cur2:
            if cur1.val + cur2.val + carry >=10:
                cur1.val = cur1.val + cur2.val + carry - 10
                carry = 1
            else:
                cur1.val = cur1.val + cur2.val + carry
                carry = 0
            current.next = cur1
            cur1 = cur1.next
            cur2 = cur2.next
            current = current.next
        
        while cur1:
            if cur1.val + carry >= 10:
                cur1.val = cur1.val + carry - 10
                carry = 1
            else:
                cur1.val = cur1.val + carry
                carry = 0
            current.next = cur1
            cur1 = cur1.next
            current = current.next
        while cur2:
            if cur2.val + carry >= 10:
                cur2.val = cur2.val + carry - 10
                carry = 1
            else:
                cur2.val = cur2.val + carry
                carry = 0
            current.next = cur2
            cur2 = cur2.next
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next
        