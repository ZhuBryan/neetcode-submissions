# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        while l1 or l2:
            if not l1:
                total = l2.val + carry
                carry = total // 10
                dig = total % 10
                new = ListNode(dig)
                l2 = l2.next
            elif not l2:
                total = l1.val + carry
                carry = total // 10
                dig = total % 10
                new = ListNode(dig)
                l1 = l1.next
            else:
                sum = l1.val + l2.val + carry
                carry = sum//10
                dig = sum % 10
                new = ListNode(dig)
                l1 = l1.next
                l2 = l2.next
            tail.next = new
            tail = tail.next
        if carry:
            tail.next = ListNode(carry)
        return dummy.next