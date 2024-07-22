# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict

class Queue:
    def __init__(self):
        self.queue = deque()

    def isEmpty(self) -> bool:
        return len(self.queue) == 0
    
    def length(self) -> int:
        return len(self.queue)

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

    def markParent(self, root: Optional[TreeNode], parent_map: dict) -> None:
        """
            This function does a BFS on the entire tree and as it iterates it stores the parent child relation
            in parent_map dictionary
        """

        if not root:
            return None

        queue: Queue = Queue()
        queue.enqueue(root)

        while not queue.isEmpty():
            parentNode: Optional[TreeNode] = queue.dequeue()

            if parentNode.left:
                parent_map[parentNode.left] = parentNode
                queue.enqueue(parentNode.left)
            if parentNode.right:
                parent_map[parentNode.right] = parentNode
                queue.enqueue(parentNode.right)

        return
            


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        if not root:
            return []

        parent_map: dict = defaultdict()

        # now we will do bfs to mark parent child 
        self.markParent(root, parent_map)

        # Lets do bfs from target node and travel radially outward until distance == k
        queue: Queue = Queue()
        queue.enqueue(target)
        distance: int = 0 # this signifies the distance from the target node

        # I will use a hash map to keep track of visited nodes
        visited: dict = defaultdict()
        visited[target] = True

        while not queue.isEmpty():
            
            if distance == k: break
            distance += 1

            size = queue.length()

            for i in range(size):
                currentNode: Optional[TreeNode] = queue.dequeue()

                # check if childs of node is visited
                if currentNode.left and currentNode.left not in visited:
                    visited[currentNode.left] = True
                    queue.enqueue(currentNode.left)
                if currentNode.right and currentNode.right not in visited:
                    visited[currentNode.right] = True
                    queue.enqueue(currentNode.right)
                
                # check if parent of the node is visited
                if currentNode in parent_map and parent_map[currentNode] not in visited:
                    visited[parent_map[currentNode]] = True
                    queue.enqueue(parent_map[currentNode])

        result = []

        while not queue.isEmpty():
            currentNode: Optional[TreeNode] = queue.dequeue()
            result.append(currentNode.val)

        return result






        
        