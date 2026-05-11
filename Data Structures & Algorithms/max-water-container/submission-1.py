class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # move the one with the less height
        # keep a global counter
        maxA = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            curr_A = (r - l) * min(heights[r], heights[l])
            maxA = max(curr_A, maxA)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        

        return maxA
