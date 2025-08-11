# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        left: int = 0
        right:int = 0

        q = deque([(root, 0)])

        memo = {}

        while q:
            node, col = q.popleft()
            
            if col not in memo:
                memo[col] = []
            memo[col].append(node.val)
            left = min(left, col)
            right = max(right, col)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        res = []
        for i in range(left, right + 1):
            if i in memo:
                res.append(memo[i])
        return res

        