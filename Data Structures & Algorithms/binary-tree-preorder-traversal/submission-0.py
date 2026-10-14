# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def rec(node):
            if not node:
                return []
            
            acc = [node.val]

            left = rec(node.left)
            right = rec(node.right)
            
            return acc + left + right

            

        return rec(root)