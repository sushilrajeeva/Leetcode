# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs: List[List[int]] = []
        if not root: return bfs
        queue = deque([root])

        while queue:
            size: int = len(queue)
            level: List[int] = [0] * size
            for i in range(size):
                node: Optional[TreeNode] = queue.popleft()
                level[i] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            bfs.append(level)

        return bfs



        