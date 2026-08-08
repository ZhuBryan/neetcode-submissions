# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergetwo(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        res = head
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next

            else:
                res.next = l2
                res = res.next
                l2 = l2.next
        if l1:
            res.next = l1
        elif l2:
            res.next = l2
        return head.next
            

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        merge = []
        for i in range (0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merge.append(self.mergetwo(l1, l2))
        return self.mergeKLists(merge)
        

        