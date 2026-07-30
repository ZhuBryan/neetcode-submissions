# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit = head
        tortoise = head

        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if tortoise == rabbit:
                return True
        return False