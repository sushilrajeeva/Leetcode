# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        val: int = 0
        if not root: return []

        result = []
        path = []

        def pathsToSum(root: Optional[TreeNode], val: int, path: List[int], result: List[List[int]], targetSum):
            if not root:
                return
            
            val += root.val
            path.append(root.val)

            if not root.left and not root.right:
                if val == targetSum:
                    result.append(list(path))
                

            pathsToSum(root.left, val, path, result, targetSum)
            pathsToSum(root.right, val, path, result, targetSum)
            path.pop()

        pathsToSum(root, val, path, result, targetSum)
        return result
            

        