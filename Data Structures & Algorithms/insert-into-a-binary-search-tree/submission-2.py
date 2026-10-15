# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def rec(node):
            if not node:
                return 
            
            if val <= node.val:
                if node.left:
                    rec(node.left)
                else:
                    node.left = TreeNode(val)
            
            else:
                if node.right:
                    rec(node.right)
                else:
                    node.right = TreeNode(val)
            
        rec(root)
        return root