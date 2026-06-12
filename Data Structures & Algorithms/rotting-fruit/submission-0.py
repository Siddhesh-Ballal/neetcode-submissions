class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        vis = set()
        rows, cols = len(grid), len(grid[0])
        q = deque([])      # rotten
        res = 0
        self.fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: q.append([r, c])
                if grid[r][c] == 1: self.fresh += 1

        def rot(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in vis or grid[r][c] != 1:
                return
            grid[r][c] = 2
            vis.add((r, c))
            q.append([r, c])
            self.fresh -= 1

        while q and self.fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)

            res += 1
        
        return res if self.fresh == 0 else -1
