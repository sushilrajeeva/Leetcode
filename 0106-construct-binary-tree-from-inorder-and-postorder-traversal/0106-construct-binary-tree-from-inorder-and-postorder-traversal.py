# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
            Inorder  : Left -> Root -> Right
            PreOrder : Root -> Left -> Right
            PostOrder: Left -> Right -> Root
        """
        if len(inorder) != len(postorder):
            return None

        if not postorder or not inorder:
            return None

        # Create a dictionary to store the index of each value in inorder traversal for quick lookup
        inorder_index = {value: index for index, value in enumerate(inorder)}

        # In postorder last node is always the root
        
        def build(in_left: int, in_right, post_left: int, post_right: int) -> Optional[TreeNode]:

            if post_left > post_right or in_left > in_right:
                return None
            
            root: Optional[TreeNode] = TreeNode(postorder[post_right])
            # Root index in the inorder list
            idx: int = inorder_index[root.val]

            # number of elements in the left subtree
            left_size = idx - in_left

            # Recursively build the left and right subtrees

            root.left = build(in_left, idx-1, post_left, post_left+left_size-1)
            root.right = build(idx+1, in_right, post_left + left_size, post_right-1)
            

            return root

        return build(0, len(inorder)-1, 0, len(postorder)-1)




        