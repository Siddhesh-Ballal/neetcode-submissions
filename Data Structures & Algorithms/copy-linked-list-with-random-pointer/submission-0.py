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
        hmap = {None : None}
        cur = head
        while cur:
            newnode = Node(cur.val)
            hmap[cur] = newnode
            cur = cur.next
        
        cur1 = head
        dummy = Node(0)
        cur2 = dummy
        
        while cur1:
            cur2.next = hmap[cur1]
            cur2.next.random = hmap[cur1.random]
            cur2.next.next = hmap[cur1.next]
            cur1 = cur1.next
            cur2 = cur2.next
        
        return dummy.next