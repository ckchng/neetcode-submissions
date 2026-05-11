# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        res = ListNode(0)
        cur = res
        # push the first node
        heap = []
        for l in lists:
            if l is not None:
                heapq.heappush(heap, NodeWrapper(l))

        while heap:
            from_heap = heapq.heappop(heap)
            # res_next = res.next
            cur.next = from_heap.node
            cur = cur.next


            if from_heap.node.next:
                heapq.heappush(heap, NodeWrapper(from_heap.node.next))
        

        return res.next