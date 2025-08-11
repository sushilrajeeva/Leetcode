# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        memo = set()
        for node in nodes:
            memo.add(node)
        
        def findLCA(node: 'TreeNode') -> 'TreeNode':
            if not node or node in memo:
                return node
            
            left = findLCA(node.left)
            right = findLCA(node.right)

            if left and right:
                return node
            
            return left if left else right

        return findLCA(root)
        