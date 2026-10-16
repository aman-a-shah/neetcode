# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # bfs out
        # check layer of bfs = one step 

        max_sum = 0

        def rec(node):
            if not node:
                return (0,0)

            nonlocal max_sum
        
            l_rob, l_skip = rec(node.left)
            r_rob, r_skip = rec(node.right)

            return (node.val+l_skip+r_skip, max(l_rob,l_skip) + max(r_rob, r_skip))
                
        
        return max(rec(root))

