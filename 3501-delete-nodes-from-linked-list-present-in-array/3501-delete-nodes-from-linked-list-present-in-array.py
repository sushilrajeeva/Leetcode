# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        numSet = set(nums)
        current = head
        dHead = dummy

        while current:
            next = current.next
            if current.val not in numSet:
                dHead.next = current
                current.next = None
                dHead = dHead.next
            current = next
        return dummy.next
                



        