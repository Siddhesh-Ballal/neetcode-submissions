class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        cache = [[-1] * (capacity + 1) for _ in range(len(profit))]

        def dfs(i, profit, weight, capacity):
            if i == len(profit): return 0
            if cache[i][capacity] != -1: return cache[i][capacity]

            cache[i][capacity] = dfs(i + 1, profit, weight, capacity)

            newC = capacity - weight[i]
            if newC >= 0:
                p = profit[i] + dfs(i + 1, profit, weight, newC)
                cache[i][capacity] = max(cache[i][capacity], p)
            
            return cache[i][capacity]
        
        return dfs(0, profit, weight, capacity)