# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = tortoise = head
        
        
        while hare:
            tortoise = tortoise.next

            if tortoise:
                hare = hare.next.next
            else:
                break

            if hare:
                if tortoise == hare:
                    return True
        
        return False
        