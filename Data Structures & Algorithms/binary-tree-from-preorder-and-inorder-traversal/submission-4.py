# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        idx_map = {val: i for i, val in enumerate(inorder)}

        def helper(pl, pr, il, ir):
            if pl > pr or il > ir:
                return None
            
            val = preorder[pl]
            mid = idx_map[val]
            left_size = mid - il
            right_size = ir - mid
            
                
            left_node = helper(pl+1, pl+left_size, il, il+left_size)
            right_node = helper(pl+left_size+1, pr, il+left_size+1, ir)

            return TreeNode(val, left_node, right_node)

        return helper(0,len(preorder)-1, 0,len(inorder)-1)


