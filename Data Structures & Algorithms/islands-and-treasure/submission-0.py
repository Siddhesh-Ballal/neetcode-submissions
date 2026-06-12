class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        distance = 0
        gates = deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    gates.append([r, c])
                    visited.add((r, c))
        
        def addroom(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == -1: return
            visited.add((r, c))
            gates.append([r, c])

        while gates:
            for _ in range(len(gates)):
                r, c = gates.popleft()
                grid[r][c] = distance

                addroom(r + 1, c)
                addroom(r - 1, c)
                addroom(r, c + 1)
                addroom(r, c - 1)
            
            distance += 1