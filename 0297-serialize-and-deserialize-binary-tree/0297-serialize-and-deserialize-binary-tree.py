# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import *
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
            

        return ",".join(result)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        nodes: List[int] = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        n: int = len(nodes)
        i = 1

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()

                if i < n and nodes[i] != "null":
                    node.left = TreeNode(int(nodes[i]))
                    queue.append(node.left)
                i += 1
                if i < n and nodes[i] != "null":
                    node.right = TreeNode(int(nodes[i]))
                    queue.append(node.right)
                i += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))