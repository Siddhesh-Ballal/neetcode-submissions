class Solution:
    def climbStairs(self, n: int) -> int:
        # memoization
        memo = {}
        
        
        def dp(i):
            if i in memo: return memo[i]
            if i == 0 or i == 1: 
                memo[i] = 1
                return 1
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        
        return dp(n)