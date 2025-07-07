# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class HeapNode:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val


import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # build the minHeap
        min_heap = []
        for ll in lists:
            if ll:
                heapq.heappush(min_heap, (ll.val, HeapNode(ll)))
        
        dummy: Optional[ListNode] = ListNode()
        cur: Optional[ListNode] = dummy
        while min_heap:
            val, hnode = heapq.heappop(min_heap)
            if hnode.node:
                h_next = HeapNode(hnode.node.next)
                hnode.next = None
                cur.next = hnode.node
                if h_next.node:
                    heapq.heappush(min_heap, (h_next.node.val, h_next))
                cur = cur.next
            
        return dummy.next
            

        