class MedianFinder:

    def __init__(self):
        self.nums = []
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # two heap approach: insertion with heap is o(log n)
        # add the number to max_heap
        # if max_heap top is larger than min_heap (stored with negative number):
        # then push it to min_heap
        if num is None:
            return
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)    
        else:
            heapq.heappush(self.max_heap, -num)

        if self.min_heap and self.max_heap:
            if -self.max_heap[0] > self.min_heap[0]:
                heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, num)
        
        # make sure both heaps are at most 1 len away (max_heap should be smaller)
        if not(len(self.max_heap) == len(self.min_heap)):
            if (len(self.max_heap) - len(self.min_heap)) > 1:
                # check which one is larger
                heapq.heappush(self.min_heap, -self.max_heap[0])
                heapq.heappop(self.max_heap)
            elif (len(self.min_heap) - len(self.max_heap)) > 1:
                heapq.heappush(self.max_heap, -self.min_heap[0])
                heapq.heappop(self.min_heap)

        return
        

    def findMedian(self) -> float:
        # retrive the middle number if possible, else return mean of the left and right
        if (len(self.max_heap) > len(self.min_heap)):
            return -self.max_heap[0]
        elif (len(self.max_heap) < len(self.min_heap)):
            return self.min_heap[0]
        elif (len(self.max_heap) == 0) and (len(self.min_heap) == 0):
            return None
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2