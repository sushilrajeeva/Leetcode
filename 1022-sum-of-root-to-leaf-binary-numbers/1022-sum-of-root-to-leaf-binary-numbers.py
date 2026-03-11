# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def getValue(self, string: str) -> int:
        res: int = 0
        n: int = len(string)
        for i in range(n):
            if string[i] == "1":
                res += (2 ** (n - i - 1))
        return res
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur: str) -> int:
            # If the node is None, there is no number to add.
            if root is None:
                return 0
            
            # Append the current node's value to the binary string.
            cur += str(root.val)
            
            # If we have reached a leaf, convert the binary string to an integer.
            if root.left is None and root.right is None:
                return self.getValue(cur)
            
            # Otherwise, return the sum from both left and right subtrees.
            return dfs(root.left, cur) + dfs(root.right, cur)
        
        return dfs(root, "")
