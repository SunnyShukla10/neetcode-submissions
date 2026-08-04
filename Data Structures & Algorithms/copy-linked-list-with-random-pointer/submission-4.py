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
        if not head:
            return head
        
        nodes = {} # curr_node : Node
        curr = head
        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            nodes[curr].next = nodes[curr.next] if curr.next else None
            nodes[curr].random = nodes[curr.random] if curr.random else None
            curr = curr.next
        
        return nodes[head]