# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = None
        prev = None
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0 
            sum_node = ListNode((val1 + val2 + carry)%10)

            if (val1 + val2 + carry)/10 >= 1:
                carry = 1
            else:
                carry = 0
    
            if prev:
                prev.next = sum_node
            else:
                sum_head = sum_node

            prev = sum_node
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
        
        if carry == 1:
            sum_node.next = ListNode(1, None)

        return sum_head