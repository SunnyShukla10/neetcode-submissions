# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        half2 = slow.next
        prev = slow.next = None

        while half2:
            tmp = half2.next
            half2.next = prev
            prev = half2
            half2 = tmp
        

        l1, l2 = head, prev
        while l2:
            tmp, tmp2 = l1.next, l2.next
            l1.next = l2
            l2.next = tmp
            l1,l2 = tmp,tmp2
        
