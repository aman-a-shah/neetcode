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

        end = prev

        start = prev.next.next
        save = prev.next
        prev = prev.next
        
        for _ in range(right - left):
            nxt = start.next
            start.next = prev
            prev = start
            start = nxt

        save.next = start
        end.next = prev

        return dummy.next
