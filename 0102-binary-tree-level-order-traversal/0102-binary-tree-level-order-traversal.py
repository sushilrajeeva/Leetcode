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
            raise IndexError("Can't peak at empty Queue")
        return self.queue[0]

    def enqueue(self, value: int) -> None:
        self.queue.append(value)

    def dequeue(self) -> int:
        if self.isEmpty():
            raise IndexError("Can't dequeue an empty Queue")
        return self.queue.popleft()


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []

        queue = Queue()
        queue.enqueue(root)
        queue.enqueue(None) # Marker to mark end of the level

        while not queue.isEmpty():

            currentNode = queue.dequeue() # pop the top of queue element

            if currentNode is None: # if we hit a marker check if it is empty queue

                if not queue.isEmpty():
                    result.append([])
                    queue.enqueue(None) # Add a marker at the end
            
            else:

                # if current Node is not empty then check if it is the root node
                if not result or currentNode == root:
                    result.append([currentNode.val])
                else:
                    result[-1].append(currentNode.val)

                # Check if there are left and right child, if so then enqueue them to the queue
                if currentNode.left:
                    queue.enqueue(currentNode.left)
                if currentNode.right:
                    queue.enqueue(currentNode.right)

        if not result[-1]:
            result.pop()

        return result


        