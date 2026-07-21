# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        '''

            1 -> 4 -> 3 -> 2 -> 5 -> None
                 ^         ^
                l_ptr     r_ptr
            left = 2 right = 4

            ans: 
            
            1 -> 4 -> 3 -> 2 -> 5 -> None



        '''
        
        dummy = ListNode(0, head)
        before_l_ptr = dummy

        for _ in range(left - 1):
            before_l_ptr = before_l_ptr.next
        l_ptr = before_l_ptr.next       

        r_ptr = l_ptr
        for _ in range(right - left):
            r_ptr = r_ptr.next
        after_r_ptr = r_ptr.next
        
        print(before_l_ptr.val)
        print(l_ptr.val)
        print(r_ptr.val)
        
        reversed = self.reverseList(l_ptr, after_r_ptr)
        before_l_ptr.next = reversed

        while reversed.next:
            reversed = reversed.next

        reversed.next = after_r_ptr

        return dummy.next

    def reverseList(self, head, end):
        prev, curr = None, head

        while curr != end:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
        



