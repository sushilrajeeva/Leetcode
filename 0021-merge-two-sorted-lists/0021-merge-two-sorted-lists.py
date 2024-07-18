# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        current = dummy

        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                temp = cur1
                cur1 = cur1.next
                temp.next = None
                current.next = temp
            else:
                temp = cur2
                cur2 = cur2.next
                temp.next = None
                current.next = temp
            current = current.next

        if cur1:
            current.next = cur1
        
        if cur2:
            current.next = cur2

        return dummy.next
        