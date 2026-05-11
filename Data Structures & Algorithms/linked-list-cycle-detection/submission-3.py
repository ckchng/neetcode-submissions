# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # fast pointer moves 2 steps at a time,
        # slow pointer moves 1 step at a time
        slow_pointer = head
        if head and head.next:
            fast_pointer = head.next
        else:
            return False
        while slow_pointer:
            if slow_pointer == fast_pointer:
                return True
            
            slow_pointer = slow_pointer.next
            # if fast pointer hits to null first, we end
            for _ in range(2):
                if fast_pointer is None:
                    return False
                fast_pointer = fast_pointer.next
