# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def peak(self) -> Optional[TreeNode]:
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        return self.queue[0]

    def enqueue(self, value: int) -> None:
        self.queue.append(value)

    def dequeue(self) -> Optional[TreeNode]:
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        return self.queue.popleft()

    def length(self) -> Optional[TreeNode]:
        return len(self.queue)

class Solution:

    def markParents(self, root: TreeNode, parent_map: dict) -> None:

        queue = Queue()
        queue.enqueue(root)

        while not queue.isEmpty():
            currentNode: Optional[TreeNode] = queue.dequeue()

            if currentNode.left:
                parent_map[currentNode.left] = currentNode
                queue.enqueue(currentNode.left)
            if currentNode.right:
                parent_map[currentNode.right] = currentNode
                queue.enqueue(currentNode.right)


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent_map = defaultdict()
        self.markParents(root, parent_map)

        visited = defaultdict()
        queue = Queue()

        # we will start from our target and radially go outwards 
        queue.enqueue(target)
        visited[target] = True

        current_reach = 0

        while not queue.isEmpty():

            size: int = queue.length()

            if current_reach == k: break

            current_reach += 1

            for i in range(size):
                node: Optional[TreeNode] = queue.dequeue()
                if node.left and node.left not in visited:
                    visited[node.left] = True
                    queue.enqueue(node.left)
                if node.right and node.right not in visited:
                    visited[node.right] = True
                    queue.enqueue(node.right)

                if node in parent_map and parent_map[node] not in visited:
                    visited[parent_map[node]] = True
                    queue.enqueue(parent_map[node])

        result = []

        while not queue.isEmpty():
            current: Optional[TreeNode] = queue.dequeue()
            result.append(current.val)

        return result



        