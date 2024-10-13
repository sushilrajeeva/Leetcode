from typing import *
from collections import defaultdict

class DoublyLinkedList:
    
    def __init__(self, value: List[int], previous: Optional['DoublyLinkedList'] = None, next: Optional['DoublyLinkedList'] = None):
        self.value = value
        self.previous = previous
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = defaultdict(DoublyLinkedList)

        self.head: DoublyLinkedList = DoublyLinkedList([-1, -1])
        self.tail: DoublyLinkedList = DoublyLinkedList([-1, -1])

        self.head.next = self.tail
        self.tail.previous = self.head

    def deleteNode(self, node: DoublyLinkedList) -> None:
        prev: DoublyLinkedList = node.previous
        next: DoublyLinkedList = node.next

        prev.next = next
        next.previous = prev

        node.next = None
        node.previous = None

        return None

    def insertAfterHead(self, node: DoublyLinkedList) -> None:

        next: DoublyLinkedList = self.head.next
        self.head.next = node
        node.next = next
        node.previous = self.head
        next.previous = node

        return None

    def get(self, key: int) -> int:

        if not self.map or not (key in self.map):
            return -1

        node: DoublyLinkedList = self.map.get(key)

        self.deleteNode(node)

        self.insertAfterHead(node)

        return node.value[1]
        

    def put(self, key: int, value: int) -> None:
        
        if self.map and key in self.map:
            node: DoublyLinkedList = self.map.get(key)
            node.value[1] = value
            self.deleteNode(node)
            self.insertAfterHead(node)
        
        else:
            if len(self.map) == self.capacity:
                leastNode: DoublyLinkedList = self.tail.previous
                del self.map[leastNode.value[0]]
                self.deleteNode(leastNode)
            newNode: DoublyLinkedList = DoublyLinkedList([key, value])
            self.map[key] = newNode
            self.insertAfterHead(newNode)

        return None



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)