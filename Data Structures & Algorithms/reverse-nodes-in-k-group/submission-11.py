# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        connector = dummy
        curr = head
        
        while True:
            # check k nodes exist starting from curr
            forward_check = curr
            for _ in range(k):
                if not forward_check:
                    return dummy.next
                forward_check = forward_check.next
            
            # reverse
            start = curr
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            connector.next = prev
            start.next = curr
            connector = start
