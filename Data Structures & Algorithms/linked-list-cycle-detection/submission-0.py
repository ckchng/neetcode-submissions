# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        slow_node = cur
        fast_node = cur
        
        # move the pointer two times forward
        i = 0
        while (i < 2):
            if fast_node is not None:
                if fast_node.next:
                    fast_node = fast_node.next
                else:
                    return False
            else:
                return False
            i += 1

        while slow_node:
            slow_node = slow_node.next
            i = 0
            while (i < 2):
                if fast_node.next:
                    fast_node = fast_node.next
                else:
                    return False
                i += 1

            if fast_node.next == None:
                return False
            
            if fast_node == slow_node:
                return True