# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import *
from collections import *
class Solution:
    def build_parents_map(self, node: TreeNode, parent: TreeNode, parent_map: Set[TreeNode]) -> Set[TreeNode]:
        if node:
            parent_map[node] = parent
            self.build_parents_map(node.left, node, parent_map)
            self.build_parents_map(node.right, node, parent_map)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = defaultdict(TreeNode)
        self.build_parents_map(root, None, parent_map)

        # bfs

        queue = deque([(target, 0)])
        visited: Set[TreeNode] = set([target])

        while queue:
            if queue[0][1] == k:
                return [node.val for node, distance in queue]
            size = len(queue)
            for _ in range(size):
                node, distance = queue.popleft()
                for neighbor in (node.left, node.right, parent_map.get(node, None)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))

        return []
        