# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0

        queue = deque([(root, 0)])

        while queue:
            size = len(queue)
            head_node, head_index = queue[0]
            for i in range(size):
                node, index = queue.popleft()
                _index = index - head_index

                if node.left:
                    queue.append((node.left, 2 * _index))
                if node.right:
                    queue.append((node.right, 2 * _index + 1))

            if queue:
                width = queue[-1][1] - queue[0][1] + 1
            else:
                width = 1
            
            max_width = max(max_width, width)

        return max_width




        