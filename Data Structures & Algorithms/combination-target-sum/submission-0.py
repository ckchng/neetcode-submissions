class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort the array o(log t)
        res = []
        nums.sort()
        
        def backtrack(start, current, remaining):
            if remaining == 0:
                res.append(list(current))
                return
            
            for i in range(start, len(nums)):
                if nums[i] > remaining: # since it's sorted
                    break

                current.append(nums[i])
                backtrack(i, current, remaining=remaining - nums[i])
                current.pop()

            return
        
        backtrack(0, [], target)

        return res