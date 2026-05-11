class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        # while (nums):
        for id, num in enumerate(nums):
             # take the first number
            if num > 0:
                break

            if id > 0 and num == nums[id - 1]:
                continue

            l = id + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -num:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] < -num:
                    l += 1
                elif nums[l] + nums[r] > -num:
                    r -=1

        return output