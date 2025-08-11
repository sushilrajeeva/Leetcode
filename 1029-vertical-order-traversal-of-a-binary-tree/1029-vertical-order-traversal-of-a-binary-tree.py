# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from collections import *
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col_map = defaultdict(list)
        queue = deque([(root, 0, 0)]) # (root, row, col)
        left = 0
        right = 0

        while queue:
            node, row, col = queue.popleft()
            col_map[col].append((row, node.val))
            left = min(left, col)
            right = max(right, col)

            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        result = []

        for col in sorted(col_map.keys()):
            col_map[col].sort()
            result.append([val for row, val in col_map[col]])
        
        return result
        