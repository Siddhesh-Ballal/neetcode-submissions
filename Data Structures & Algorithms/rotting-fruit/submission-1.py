class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set() 
        time = 0
        queue = deque([])
        self.fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: queue.append([r, c])
                elif grid[r][c] == 1: self.fresh += 1

        def rot(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] != 1: return
        
            visited.add((r, c)) 
            queue.append([r, c])
            grid[r][c] = 2
            self.fresh -= 1

        while queue and self.fresh:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                rot(r + 1, c)
                rot(r, c + 1)
                rot(r - 1, c)
                rot(r, c - 1)
        
            time += 1
        
        return time if self.fresh == 0 else -1