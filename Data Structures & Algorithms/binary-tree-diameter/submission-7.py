# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diam = 0

        def rec(node):
            nonlocal diam
            if not node:
                return 0
                
            left = rec(node.left)
            right = rec(node.right)

            diam = max(diam, left+right)
            return max(left+1, right+1)
        
        rec(root)
        return diam