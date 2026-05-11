class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_hash = Counter(nums)
        bucket_sort = [[] for _ in range(len(nums))]
        for id, val in num_hash.items():
            bucket_sort[val-1].append(id) # multiple numbers can share the same freq
        
        
        # go through from largest freq to lowest
        res = []
        for i in range(len(nums)-1, -1, -1):
            if bucket_sort[i]:
                for num in bucket_sort[i]:
                    res.append(num)
                    k -= 1
                    if k == 0:
                        return res
