# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 1. find mid
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse 2nd half
        prev = None
        curr = slow.next
        slow.next = prev
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. weave
        curr1 = head
        curr2 = prev

        while curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next

            curr1.next = curr2
            curr2.next = nxt1

            curr1 = nxt1
            curr2 = nxt2