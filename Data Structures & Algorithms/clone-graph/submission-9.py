"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        visited = {}

        def clone(node: Node):
            nonlocal visited

            neighbours = []
            cloned = Node(node.val)
            visited[node] = cloned

            for neighbour in node.neighbors:
                if neighbour not in visited:
                    neighbours.append(clone(neighbour))
                else:
                    neighbours.append(visited[neighbour])
            
            cloned.neighbors = neighbours
            return visited[node]

        return clone(node)

        
