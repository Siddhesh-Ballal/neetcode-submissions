class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[-2], cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            t = a
            a = cost[i] + min(a, b)
            b = t
        return min(a, b)