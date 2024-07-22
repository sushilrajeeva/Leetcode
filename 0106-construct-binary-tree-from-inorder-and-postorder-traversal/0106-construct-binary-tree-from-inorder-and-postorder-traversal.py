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

        inorder_hash: dict = defaultdict()
        for i in range(len(inorder)):
            inorder_hash[inorder[i]] = i
        
        def build(inorder: List[int], inStart: int, inEnd: int, postOrder: List[int], postStart: int, postEnd: int, inorder_hash: dict) -> Optional[TreeNode]:

            # Checking if we got valid indexes
            if inStart > inEnd or postStart > postEnd:
                return None

            # We know that the last element of the post order is the root
            root: Optional[TreeNode] = TreeNode(postOrder[postEnd])
            rootIndex: int = inorder_hash[root.val]

            # Number of nodes left in the left subtree
            leftRange: int = rootIndex - inStart

            # Recursively building the tree
            root.left = build(inorder, inStart, rootIndex-1, postOrder, postStart, postStart + leftRange -1, inorder_hash)
            root.right = build(inorder, rootIndex + 1, inEnd, postOrder, postStart + leftRange, postEnd-1, inorder_hash)

            return root

        root: optional[TreeNode] = build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, inorder_hash)

        return root


        