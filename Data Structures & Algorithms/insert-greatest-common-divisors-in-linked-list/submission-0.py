# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = head

        def gcd(unit, num):
            for i in range(unit, 0, -1):
                if unit % i == 0 and num % i == 0:
                    return i

        while curr:
            curr_gcd = gcd(prev.val, curr.val) if prev.val < curr.val else gcd(curr.val, prev.val)

            node = ListNode(curr_gcd, curr)
            prev.next = node
            prev = curr
            curr = curr.next
        
        return head

