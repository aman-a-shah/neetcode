"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def rec(row, col, size):

            if size == 1:
                return Node(bool(grid[row][col]), True)
            
            rec_size = size//2
            tl = rec(row, col, rec_size)
            tr = rec(row, col+rec_size, rec_size)
            bl = rec(row+rec_size, col, rec_size)
            br = rec(row+rec_size, col+rec_size, rec_size)

            same_val = tl.val == tr.val == bl.val == br.val
            all_leaf = tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
            if all_leaf and same_val:
                return Node(tl.val, True)
            else:
                return Node(True, False, tl, tr, bl, br)

        return rec(0, 0, len(grid))