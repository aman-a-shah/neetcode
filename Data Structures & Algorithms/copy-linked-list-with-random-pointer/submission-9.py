"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # 1. create a copy of each node in hash map with val:node
        mp = {}
        curr = head
        prev = None
        head_copy = None
        while curr:
            new_node = Node(curr.val)
            mp[curr] = new_node
            if prev:
                prev.next = new_node
            else:
                head_copy = new_node
            prev = new_node
            curr = curr.next

        # 2. go through list and build out full copy
        curr = head
        curr_copy = head_copy
        while curr:
            if curr.random:
                curr_copy.random = mp[curr.random]
            curr = curr.next
            curr_copy = curr_copy.next
        
        return head_copy




