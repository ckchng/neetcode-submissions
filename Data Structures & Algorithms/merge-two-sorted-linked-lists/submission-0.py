# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy

        while list1 or list2: # as long as there are still nodes in the lists
            if list1 is None:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            elif list2 is None:
                tail.next = ListNode(list1.val)
                list1 = list1.next                
            elif list1.val <= list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            tail = tail.next

        return dummy.next