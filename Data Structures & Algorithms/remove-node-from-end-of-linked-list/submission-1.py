# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0, head)
        near = dum
        far = dum
        i = n
        while far.next:
            if i <= 0:
                near = near.next
            else:
                i -= 1
            far = far.next
    
        near.next = near.next.next
        return dum.next

        