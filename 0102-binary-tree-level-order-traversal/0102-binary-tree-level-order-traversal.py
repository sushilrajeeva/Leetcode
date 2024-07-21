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

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def peak(self) -> int:
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.queue[0]

    def enqueue(self, value) -> None:
        self.queue.append(value)

    def dequeue(self) -> int:
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.queue.popleft()


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []

        queue = Queue()
        queue.enqueue(root)
        queue.enqueue(None)

        while not queue.isEmpty():

            currentNode = queue.dequeue()

            # Condition - when current Node is Empty / None
            if currentNode is None:
                if not queue.isEmpty():
                    result.append([])
                    queue.enqueue(None)

            # Condition - when current Node is not Empty
            else:
                
                # check if result is empty or if it is the root node
                if not result or root == currentNode:
                    result.append([currentNode.val])
                else:
                    result[-1].append(currentNode.val)

                if currentNode.left:
                    queue.enqueue(currentNode.left)
                if currentNode.right:
                    queue.enqueue(currentNode.right)


        if not result[-1]:
            result.pop()

        return result
        