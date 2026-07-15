class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        vis = set()
        res = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in vis or grid[r][c] == 0: return 0
            vis.add((r, c))
            cur = 1
            cur += dfs(r + 1, c)
            cur += dfs(r, c + 1)
            cur += dfs(r - 1, c)
            cur += dfs(r, c - 1)
            return cur
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in vis:
                    res = max(res, dfs(r, c))
        
        return res