# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Queue:

    def __init__(self):
        self.queue = deque()
    
    def isEmpty(self) -> bool:
        return len(self.queue)==0

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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        level_items = defaultdict(list)

        queue = Queue()
        queue.enqueue((0, 0, root))

        min_col, max_col = float("inf"), float("-inf")

        result = []

        while not queue.isEmpty():

            col, row, node = queue.dequeue()

            level_items[col].append((row, node.val))

            min_col = min(min_col, col) # to keep track of minimum edge / boundry
            max_col = max(max_col, col) # to keep track of maximum edge / boundry

            if node.left:
                queue.enqueue((col - 1, row + 1, node.left))
            if node.right:
                queue.enqueue((col + 1, row + 1, node.right))
        
        def sortFunc(arr):
            row, node = arr[0], arr[1]
            return row


        for level in range(min_col, max_col + 1):
            # Sort by row first, then by value if rows are the same
            level_items[level].sort(key=lambda x: (x[0], x[1]))
            result.append([val for row, val in level_items[level]])

        return result




        