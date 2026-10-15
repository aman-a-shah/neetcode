class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1 & 2: no left child or no right child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: two children
            # Find in-order successor (min of right subtree)
            succ = root.right
            while succ.left:
                succ = succ.left
            
            # Replace value with successor's value
            root.val = succ.val
            # Delete the successor from the right subtree
            root.right = self.deleteNode(root.right, succ.val)
        
        return root