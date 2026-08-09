# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevtail = dummy
        while head:
            count = 0
            curr = head
            while curr and count < k:
                curr = curr.next
                count += 1
            if count < k:
                break

            prev = None
            curr = head
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            prevtail.next = prev
            head.next = curr
            prevtail = head
            head = curr
        return dummy.next