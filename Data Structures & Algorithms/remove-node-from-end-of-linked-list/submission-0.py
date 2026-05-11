# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        for i in range(n):
            fast = fast.next

        # if there is only 1 node
        if fast is None:
            return head.next

        # print(slow.val)
        # print(fast.val)
        prev = slow
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next

        return head