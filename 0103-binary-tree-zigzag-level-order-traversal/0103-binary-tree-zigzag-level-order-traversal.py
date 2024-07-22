from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Queue:
    def __init__(self):
        self.queue = deque()

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def peek(self) -> Optional[TreeNode]:
        if not self.isEmpty():
            return self.queue[0]
        raise IndexError("Queue is Empty")
    
    def enqueue(self, value: TreeNode) -> None:
        self.queue.append(value)

    def dequeue(self) -> Optional[TreeNode]:
        if not self.isEmpty():
            return self.queue.popleft()
        raise IndexError("Queue is Empty")

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = Queue()
        queue.enqueue(root)
        queue.enqueue(None)
        current_level = []
        left_to_right = True

        while not queue.isEmpty():
            currentNode = queue.dequeue()

            if currentNode is None:
                if not queue.isEmpty():
                    if not left_to_right:
                        current_level.reverse()
                    result.append(current_level)
                    current_level = []
                    left_to_right = not left_to_right
                    queue.enqueue(None)
            else:
                current_level.append(currentNode.val)
                if currentNode.left:
                    queue.enqueue(currentNode.left)
                if currentNode.right:
                    queue.enqueue(currentNode.right)

        if current_level:
            if not left_to_right:
                current_level.reverse()
            result.append(current_level)

        return result
