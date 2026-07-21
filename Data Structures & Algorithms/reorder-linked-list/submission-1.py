# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        # find the midpoint of the list
        #   - Can use the fast and slow approach
        
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        half2 = slow.next 
        slow.next = None

        # reverse the 2nd half of the list
        prev = None

        while half2:
            nxt = half2.next
            half2.next = prev
            prev = half2
            half2 = nxt
        
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2