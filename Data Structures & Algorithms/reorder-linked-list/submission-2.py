# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        slow, fast = head, head
        mid_node = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            mid_node = slow

        prev = None
        cur = mid_node
        while cur: 
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        fast = head
        slow = prev
        while slow and slow.next:
            fast_next_tmp = fast.next
            fast.next = slow
            slow_next_tmp = slow.next
            slow.next = fast_next_tmp
            fast = fast_next_tmp
            slow = slow_next_tmp
            