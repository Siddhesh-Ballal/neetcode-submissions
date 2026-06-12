class Solution:
    def linrob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for n in nums:
            t = max(a + n, b)
            a = b
            b = t
        return t

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.linrob(nums[:-1]), self.linrob(nums[1:]))