# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def rec(node):
            if not node:
                return 0
            left = rec(node.left)
            if left == -1:
                return -1
            right = rec(node.right)
            if right == -1:
                return -1
            if abs(left-right)>1:
                return -1
            return max(left, right) + 1

        return rec(root) != -1
    