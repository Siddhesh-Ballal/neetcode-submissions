class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        positive_diagonals = set()   # r + c
        negative_diagonals = set()   # r - c

        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            
            for col in range(n):
                if col in cols or row + col in positive_diagonals or row - col in negative_diagonals:
                    continue
                
                cols.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                cols.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return res
