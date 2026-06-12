class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board) , len(board[0])
        o = len(word)
        mark=[[0] * n for _ in range(m)]
        def dfs(row , col , index):
            if index == o:
                return True
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if mark[row][col] == 1:
                return False
            if board[row][col] != word[index]:
                return False

            mark[row][col] = 1
            found = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
            )
            mark[row][col] = 0
            return found

            
            return False
        for row in range(m):
            for col in range(n):
                if dfs(row, col, 0):
                    return True

        return False
