class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def traverse(i, sub):
            if i == len(nums):
                res.append(sub)
                return
            # skip
            traverse(i + 1, sub)
            # take
            traverse(i + 1, sub + [nums[i]])
        traverse(0, [])
        return res