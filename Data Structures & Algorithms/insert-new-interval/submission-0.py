class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # check for boundary first
        # for each interval, check for 3 cases.
        # whether it's before, overlap, or after.
        # if it's before, then insert both into the result
        # if it overlaps, merge them, dont insert yet.
        # if it's after, then insert both into the result

        # handle the before and after first
        # check for boundary first
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # can only be executed once
                res.append(newInterval)
                return res + intervals[i:] 
            elif newInterval[0] > intervals[i][1]:# if it's completely larger than then current interval
                res.append(intervals[i])
            else: # overlap
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            
        res.append(newInterval)
    
        return res