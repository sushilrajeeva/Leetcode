# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def helper(root) -> str:
            if not root: return "_"

            left = helper(root.left)
            right = helper(root.right)
            return str(root.val) + "," + left + "," + right

        res = ""
        res = helper(root)

        print("res", res)
        return res

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        decode_list = data.split(",")

        print("decode_list", decode_list)

        def helper(index):
            if decode_list[index] == "_":
                return None, index + 1
            
            node = TreeNode(decode_list[index])

            node.left, next_index = helper(index + 1)
            node.right, next_index = helper(next_index)

            return node, next_index

        root, next_index = helper(0)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))