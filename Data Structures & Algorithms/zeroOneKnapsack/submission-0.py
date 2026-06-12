class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        def dfs(i, profit, weight, capacity):
            if i == len(profit): return 0
            
            maxP = dfs(i + 1, profit, weight, capacity)

            newC = capacity - weight[i]
            if newC >= 0:
                p = profit[i] + dfs(i + 1, profit, weight, newC)
                maxP = max(maxP, p) 
            
            return maxP
        
        return dfs(0, profit, weight, capacity)