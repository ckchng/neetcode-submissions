class Solution:
    def climbStairs(self, n: int) -> int:
        # the key idea is that, after every step you take, you have two choices, take 1 step or 2.
        # ways(n) = ways(n - 1) + ways(n - 2)
        # it's like you do DFS, but when you come back up, you can search through a dict to see if the route has been explored
        memo = {}
        def helper(i):
            if i == 0:
                return 1
            if i == 1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = helper(i - 1) + helper(i - 2)
            return memo[i]
        
        return helper(n)
        
