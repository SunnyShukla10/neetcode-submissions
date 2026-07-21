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
        
        d = {None : None}
        
        pass1 = head
        while pass1:
            copy = Node(pass1.val)
            d[pass1] = copy
            pass1 = pass1.next
        
        pass2 = head
        while pass2:
            copy = d[pass2]
            copy.next = d[pass2.next]
            copy.random = d[pass2.random]
            pass2 = pass2.next

        return d[head]