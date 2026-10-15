# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            
        heights = set()
        acc = []

        def rec(node, height):
            nonlocal heights
            nonlocal acc

            if not node:
                return []

            if height not in heights:
                heights.add(height)
                acc.append(node.val)
            rec(node.right, height+1)
            rec(node.left, height+1)

        rec(root, 0)
        return acc