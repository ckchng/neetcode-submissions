# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # fast = i + n 
        # slow = i
        # when fast reaches None, we remove slow
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        
        if fast is None:
            return head.next

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

    
        prev.next = slow.next

        return head