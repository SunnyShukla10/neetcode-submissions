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
        
        d = {None: None}
        # 2 pass
        
        # first pass instiantiate each node and put into a dictionary
        curr = head
        while curr:
            node = Node(curr.val)
            d[curr] = node 
            curr = curr.next
        
        curr = head
        while curr:
            newnode = d[curr]
            newnode.next = d[curr.next]
            newnode.random = d[curr.random]

            curr = curr.next
        
        return d[head]

        