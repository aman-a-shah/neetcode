# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []

        def rec(node):
            if not node:
                serialized.append('null')
                return
            
            serialized.append(str(node.val))

            rec(node.left)
            rec(node.right)

        rec(root)
        return ','.join(serialized)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')

        i = 0
        def rec():
            nonlocal i

            if i >= len(nodes) or nodes[i] == 'null':
                i += 1
                return None
                
            new_node = TreeNode(int(nodes[i]))
            i += 1
            left = rec()
            right = rec()

            new_node.left = left
            new_node.right = right

            return new_node
        
        return rec()



