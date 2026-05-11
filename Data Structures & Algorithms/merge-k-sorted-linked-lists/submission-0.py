# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        min_id = 0
        min_val = float('infinity')
        for i in range(len(lists)):
            if lists[i] is not None:
                if lists[i].val < min_val:
                    min_val = lists[i].val
                    min_id = i
        if min_val == float('infinity'):
            return None

        first_list = lists.pop(min_id)

        while lists:
            curr_list = lists.pop(0)
            # traverse thru first_list
            curr_node = first_list
            curr_node_k = curr_list
            
            #traverse through the curr_list
            while curr_node_k:
                # curr_val = curr_node.val
                # next_val = curr_node.next.val
                if curr_node.next is None:
                    curr_node_next = curr_node.next
                    curr_node.next = curr_node_k
                    curr_node_k_next = curr_node_k.next
                    curr_node_k.next = curr_node_next
                    curr_node = curr_node.next
                    curr_node_k = curr_node_k_next
                elif curr_node.val <= curr_node_k.val and curr_node_k.val <= curr_node.next.val: # in between
                    # insert into first_list
                    curr_node_next = curr_node.next
                    curr_node.next = curr_node_k
                    curr_node_k_next = curr_node_k.next
                    curr_node_k.next = curr_node_next
                    curr_node = curr_node.next
                    curr_node_k = curr_node_k_next
                else:
                    # move curr_node forward, but retain curr_node_k
                    curr_node = curr_node.next
                    

        return first_list    