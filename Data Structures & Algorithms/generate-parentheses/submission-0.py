class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(cur, Open, Closed):
            if Open == Closed == n:
                res.append(cur)
                return
            if Open < n:
                backtrack(cur + "(", Open + 1, Closed)
            if Closed < Open:
                backtrack(cur + ")", Open, Closed + 1)
        backtrack("", 0, 0)
        return res