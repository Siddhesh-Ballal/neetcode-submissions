class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def traverse(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O': return
            board[r][c] = 'T'
            traverse(r + 1, c)
            traverse(r - 1, c)
            traverse(r, c + 1)
            traverse(r, c - 1)
        
        for r in range(rows):
            traverse(r, 0)
            traverse(r, cols - 1)
        
        for c in range(cols):
            traverse(0, c)
            traverse(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O': board[r][c] = 'X'
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T': board[r][c] = 'O'