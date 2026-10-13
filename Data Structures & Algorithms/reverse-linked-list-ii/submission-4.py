# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        start = prev.next
        then = start.next      # node we'll repeatedly move to the front

        for _ in range(right - left):
            start.next = then.next   # detach `then`
            then.next = prev.next    # point `then` to current front of reversed section
            prev.next = then         # make `then` the new front
            then = start.next        # advance `then`

        return dummy.next
