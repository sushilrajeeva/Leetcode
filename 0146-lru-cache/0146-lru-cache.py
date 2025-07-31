from typing import *
class ListNode:
    def __init__(self, key: int, val: int, previous = None, next = None):
        self.key = key
        self.val = val
        self.previous = previous
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, Optional[ListNode]] = {}
        self.head: ListNode = ListNode(-1, -1)
        self.tail: ListNode = ListNode(-2, -2)
        self.head.next = self.tail
        self.tail.previous = self.head

    def move_to_end(self, node: Optional[ListNode]):
        lastNode: ListNode = self.tail.previous

        lastNode.next = node
        node.previous = lastNode

        node.next = self.tail
        self.tail.previous = node

    def rewire_pointers(self, node: Optional[ListNode]):
        before: ListNode = node.previous
        after: ListNode = node.next

        before.next = after
        after.previous = before
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node: ListNode = self.cache[key]
        value: int = node.val

        self.rewire_pointers(node)
        self.move_to_end(node)

        return value
        

    def put(self, key: int, value: int) -> None:

        node: Optional[ListNode] = None
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.rewire_pointers(node)
        else:
            node = ListNode(key, value)
        self.cache[key] = node
        self.move_to_end(node)

        if len(self.cache) > self.capacity:
            lruNode: ListNode = self.head.next
            self.rewire_pointers(lruNode)
            del self.cache[lruNode.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)