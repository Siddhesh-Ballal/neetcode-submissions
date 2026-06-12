class Solution:
    def dfs(self, r, c, grid, visited):
        rows = len(grid)
        cols = len(grid[0])
        if (r < 0 or c < 0) or (r == rows or c == cols) or ((r, c) in visited) or (grid[r][c] == 1):
            return 0
        elif (r == rows - 1 and c == cols - 1):
            return 1
        
        visited.add((r, c))
        count = 0
        count += self.dfs(r + 1, c, grid, visited)
        count += self.dfs(r, c + 1, grid, visited)
        count += self.dfs(r, c - 1, grid, visited)
        count += self.dfs(r - 1, c, grid, visited)
        visited.remove((r, c))

        return count

    def countPaths(self, grid: List[List[int]]) -> int:
        return self.dfs(0, 0, grid, set())