class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first hash
        tab = {}
        for num in nums:
            if num in tab:
                tab[num] += 1
            else:
                tab[num] = 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in tab.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            if bucket[i]:
                res.extend(bucket[i])
                if len(res) >= k:
                    return res[:k]
