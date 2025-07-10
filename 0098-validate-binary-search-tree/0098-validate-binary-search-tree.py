# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        stack = deque([(root, float("-inf"), float("inf"))])

        while stack:
            
            size = len(stack)
            for _ in range(size):
                node, lower, upper = stack.popleft()
                val = node.val
                if val <= lower or val >= upper:
                    return False
                if node.left:
                    stack.append((node.left, lower, val))
                if node.right:
                    stack.append((node.right, val, upper))
            
        return True
        