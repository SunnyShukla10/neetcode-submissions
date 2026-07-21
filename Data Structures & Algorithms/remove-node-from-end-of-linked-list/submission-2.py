# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head

        dummy = ListNode(0, node)

        while n > 0:
            node = node.next
            n-=1
        
        left = dummy

        while node:
            node = node.next
            left = left.next
        left.next = left.next.next
        return dummy.next