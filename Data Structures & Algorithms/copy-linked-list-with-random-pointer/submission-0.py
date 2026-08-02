"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        tail = dummy
        curr = head
        randoms = {}
        while curr:
        
            new = Node(curr.val)
            randoms[curr] = new
            curr = curr.next
            tail.next = new
            tail = tail.next

        curr = head
        ncurr = dummy.next
        while ncurr:
            if curr.random:
                randoms[curr].random = randoms[curr.random]
            ncurr = ncurr.next
            curr = curr.next
        return dummy.next
