# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    assumption:
        1. a node can be descended of itself
        2. node val -> always number
        3. node val are any , and just a tree not bst
        4. number of nodes ? large -> n

    root = 1
    p = 6
    q = 5
                [1]
            [2]      [3]
        [6]     [4]        [5]

TC: O(N)
SC: O(N)
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right


        