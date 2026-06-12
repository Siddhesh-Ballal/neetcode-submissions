class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set() 
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))
        length = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == rows - 1 and col == cols - 1:
                    return length
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if nr not in range(rows) or nc not in range(cols) or (nr, nc) in visited or grid[nr][nc] == 1:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1