# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
            PreOrder = Root -> Left -> Right
            Inorder = Left -> Root -> Right
            PostOrder = Left -> Right -> Root
        """

        inorder_hash: dict = defaultdict()
        # key = node data and value is the index at which this node exist in inorder
        for i in range(len(inorder)):
            inorder_hash[inorder[i]] = i

        def build(preorder: List[int], preStart: int, preEnd: int, inorder: List[int], inStart: int, inEnd: int, inorder_hash: dict) -> Optional[TreeNode]:

            # exit condition
            if preStart > preEnd or inStart > inEnd:
                return None
            
            # constructing root node [first element in preorder is the root]
            root: Optional[TreeNode] = TreeNode(preorder[preStart])

            rootIndex: int = inorder_hash[root.val]
            leftRange: int = rootIndex - inStart

            root.left = build(preorder, preStart + 1, preStart + leftRange, inorder, inStart, rootIndex - 1, inorder_hash)
            root.right = build(preorder, preStart + leftRange + 1, preEnd, inorder, rootIndex + 1, inEnd, inorder_hash)

            return root

        root: Optional[TreeNode] = build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inorder_hash)

        return root

        


        