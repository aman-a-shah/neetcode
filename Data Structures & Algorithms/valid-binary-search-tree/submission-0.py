# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def rec(node, low, high):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            else:
                left = rec(node.left, low, node.val) 
                right = rec(node.right, node.val, high)

                if not left or not right:
                    return False
                else:
                    return True
            
        return rec(root, -float('inf'), float('inf'))