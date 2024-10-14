from typing import *
from collections import defaultdict

class Node:

    def __init__(self, value: List[int], previous: 'Node' = None, next: 'Node' = None):
        self.value = value
        self.previous = previous
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = defaultdict(Node)
        self.head = Node([-1, -1])
        self.tail = Node([-1, -1])

        self.head.next = self.tail
        self.tail.previous = self.head

    def deleteNode(self, node: Node) -> None:

        if not node: return None

        prev: Node = node.previous
        next: Node = node.next

        prev.next = next
        next.previous = prev

        node.next = None
        node.previous = None

    
    def insertNode(self, node: Node) -> None:

        if not node: return None

        first: Node = self.head
        second: Node = self.head.next

        first.next = node
        node.previous = first

        second.previous = node
        node.next = second

    def get(self, key: int) -> int:

        # edge case - key not present
        if key not in self.map:
            return -1

        node: Node = self.map.get(key)
        self.deleteNode(node)
        self.insertNode(node)

        return node.value[1]
        

    def put(self, key: int, value: int) -> None:

        # Edge case - if capacity is full
        if key in self.map:
            # Update the existing node and move it to the front
            node = self.map[key]
            node.value[1] = value
            self.deleteNode(node)
            self.insertNode(node)
        else:
            if len(self.map) == self.capacity:
                # Remove the least recently used node (before tail)
                lru_node = self.tail.previous
                self.deleteNode(lru_node)
                del self.map[lru_node.value[0]]  # Remove from map
            # Insert new node
            new_node = Node([key, value])
            self.map[key] = new_node
            self.insertNode(new_node)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)