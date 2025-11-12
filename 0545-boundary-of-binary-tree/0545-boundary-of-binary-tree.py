# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _is_leaf(self,node):
        return node and node.left is None and node.right is None 

    def add_leaves(self,node, res):
            if not node:
                return None

            if self._is_leaf(node):
                res.append(node.val)
                return

            self.add_leaves(node.left, res)
            self.add_leaves(node.right, res)


    def boundaryOfBinaryTree(self, root):
        if not root:
            return []
        
        res = []

        res.append(root.val)

        # -- > left boundary <--- 
        cur = root.left

        while cur :
            if not self._is_leaf(cur):
                res.append(cur.val)

            cur = cur.left if cur.left else cur.right


        #---> leaves < ----

        self.add_leaves(root.left, res)
        self.add_leaves(root.right, res)


        # --> right boundary <---

        stack = []
        curr = root.right

        while curr:
            if not self._is_leaf(curr):
                stack.append(curr.val)
            
            curr = curr.right if curr.right else curr.left

        while stack:
            res.append(stack.pop())
    
        return res

        