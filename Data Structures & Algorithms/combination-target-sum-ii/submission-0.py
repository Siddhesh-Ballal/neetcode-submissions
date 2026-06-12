class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, sub, subsum):
            if subsum == target:
                res.append(sub)
                return
            if i == len(candidates) or subsum > target: return
            # take
            dfs(i + 1, sub + [candidates[i]], subsum + candidates[i])
            # skip
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sub, subsum)
        dfs(0, [], 0)
        return res