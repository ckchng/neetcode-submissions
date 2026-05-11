# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # add the min of the two values from the list into the LL, use pointer
        head = ListNode(0)
        curr_node = head
        while list1 or list2:
            if list1 is None:
                val_to_be_added = list2.val
                list2 = list2.next
            elif list2 is None:
                val_to_be_added = list1.val
                list1 = list1.next
            elif list1.val < list2.val:
                val_to_be_added = list1.val
                list1 = list1.next
            else:
                val_to_be_added = list2.val
                list2 = list2.next
                
            curr_node.next = ListNode(val_to_be_added)
            curr_node = curr_node.next

        return head.next