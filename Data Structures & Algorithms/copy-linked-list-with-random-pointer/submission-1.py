"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hmap = {}
        cur = head
        while cur:
            hmap[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while(cur):
            nc = hmap[cur]
            nc.next = hmap.get(cur.next)
            nc.random = hmap.get(cur.random)
            cur=cur.next
        return hmap[head]