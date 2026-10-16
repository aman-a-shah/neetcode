# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def should_pop(node):
            if not node:
                return False
            
            left = should_pop(node.left)
            right = should_pop(node.right)
            
            if left:
                node.left = None
            if right:
                node.right = None

            if not node.left and not node.right:
                if node.val == target:
                    return True
            
            return False

        should_pop = should_pop(root)
        if should_pop:
            return None
        return root
