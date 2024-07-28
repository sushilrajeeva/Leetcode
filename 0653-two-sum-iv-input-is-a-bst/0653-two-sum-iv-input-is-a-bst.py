# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def isTargetPresent(root: Optional[TreeNode], k: int) -> bool:

            if not root:
                return False
            
            if k-root.val in seen:
                return True
            
            seen.add(root.val)
            
            left = isTargetPresent(root.left, k)
            if left: return True
            right = isTargetPresent(root.right, k)
            if right: return True
            return False

        return isTargetPresent(root, k)
        