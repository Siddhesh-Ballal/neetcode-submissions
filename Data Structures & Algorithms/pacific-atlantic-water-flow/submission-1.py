class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atlantic_visit, pacific_visit = set(), set()

        def dfs(r, c, visit, prvheight):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or heights[r][c] < prvheight: return 
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pacific_visit, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pacific_visit, heights[r][0])
        
        for c in range(cols):
            dfs(rows - 1, c, atlantic_visit, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atlantic_visit, heights[r][cols - 1])


        return list(pacific_visit & atlantic_visit)