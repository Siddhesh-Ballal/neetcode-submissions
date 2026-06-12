class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def traverse(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == '0':
                return 
            grid[r][c] = '0'
            traverse(r + 1, c)
            traverse(r - 1, c)
            traverse(r, c + 1)
            traverse(r, c - 1)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    traverse(r, c)
        
        return res