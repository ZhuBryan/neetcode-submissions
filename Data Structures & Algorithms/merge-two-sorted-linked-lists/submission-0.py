# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode()
        res = dum
        while list1 or list2:
            if not list2 or (list1 and list1.val <= list2.val):
                res.next = list1
                list1 = list1.next
                res = res.next
            else:
                res.next = list2
                list2 = list2.next
                res = res.next
        return dum.next
