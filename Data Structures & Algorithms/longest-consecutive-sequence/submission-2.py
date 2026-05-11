class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # hash it
        tab = set()
        for num in nums:
            tab.add(num)

        begin_nums = {}
        for num in tab:
            if num - 1 in tab:
                continue
            else:
                # it's the beginning number
                begin_nums[num] = []
        
        longest_con = 0
        for num in tab:
            smallest_diff = 10000
            if num not in begin_nums:
                for begin_num, _ in begin_nums.items():
                    diff = num - begin_num
                    if diff > 0 and diff < smallest_diff:
                        smallest_diff = diff
                        closest_num = begin_num
            
                # end the end of it, append
                begin_nums[closest_num].append(num)
                if len(begin_nums[closest_num]) > longest_con:
                    longest_con = len(begin_nums[closest_num])

        return longest_con + 1