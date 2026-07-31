# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow
        while cur:
            then = cur.next
            cur.next = prev
            prev = cur
            cur = then
        fir = head
        stop = prev
        sec = prev

        while sec and sec.next:
            temp = fir.next
            fir.next = sec
            fir = temp
            setemp = sec.next
            sec.next = fir
            sec = setemp

        return
        