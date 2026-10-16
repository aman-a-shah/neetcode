# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = -float('inf')

        def rec(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left = rec(node.left)
            right = rec(node.right)

            max_sum = max([max_sum, left+right+node.val, left+node.val, right+node.val, node.val])

            return max([left+node.val, right+node.val, node.val])
        
        return max(rec(root), max_sum)

        