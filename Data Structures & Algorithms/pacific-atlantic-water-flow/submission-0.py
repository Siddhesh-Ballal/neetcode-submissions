class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, prevHeight, vis):
            if r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight or (r, c) in vis: return
            vis.add((r, c))
            dfs(r + 1, c, heights[r][c], vis)
            dfs(r - 1, c, heights[r][c], vis)
            dfs(r, c + 1, heights[r][c], vis)
            dfs(r, c - 1, heights[r][c], vis)
        
        for c in range(cols):
            dfs(0, c, heights[0][c], pacific)
            dfs(rows - 1, c, heights[rows - 1][c], atlantic)
        
        for r in range(rows):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, cols - 1, heights[r][cols - 1], atlantic)
        
        return list(pacific & atlantic)