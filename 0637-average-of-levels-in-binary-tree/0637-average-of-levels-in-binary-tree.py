# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    def length(self) -> int:
        return len(self.queue)
    def isEmpty(self) -> bool:
        return len(self.queue) == 0
    def peak(self) -> Optional[TreeNode]:
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.queue[0]
    def enqueue(self, value: int) -> None:
        self.queue.append(value)
    def dequeue(self) -> Optional[TreeNode]:
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.queue.popleft()


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return [0.0]
        
        queue: Queue = Queue()
        queue.enqueue(root)
        queue.enqueue(None)

        averages = []
        total: int = 0
        count: int = 0
        while not queue.isEmpty():

            node: Optional[TreeNode] = queue.dequeue()

            if node is None:
                if count > 0:
                    averages.append(total / count)
                total = 0
                count = 0
                if not queue.isEmpty():
                    queue.enqueue(None)
            else:
                total += node.val
                count += 1
                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
        
        return averages



        