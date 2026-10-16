# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0

        def bfs(node, largest_val):
            if not node:
                return

            nonlocal good_nodes

            if node.left or node.right:
                bfs(node.left, max(largest_val, node.val))
                bfs(node.right, max(largest_val, node.val))
                
            if node.val >= largest_val:
                good_nodes += 1
                
        bfs(root, -float('inf'))
        return good_nodes