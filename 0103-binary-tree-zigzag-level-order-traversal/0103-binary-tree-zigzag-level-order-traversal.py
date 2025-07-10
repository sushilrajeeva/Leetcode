# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag: bool = True
        queue = deque([root])
        res: List[List[int]] = []
        if not root: return res

        while queue:
            level_len = len(queue)
            level = deque()
            for i in range(level_len):
                node: Optional[TreeNode] = queue.popleft()
                if flag:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            flag  = False if flag else True
            res.append(list(level))
        
        return res





        