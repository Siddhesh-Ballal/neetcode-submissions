class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            # return if we are at target
            if nums[m] == target: return m
            
            # m is in left sorted
            if nums[m] > nums[r]:
                # if target is less than nums[l] OR target is > m, go right
                if target < nums[l] or target > nums[m]: l = m + 1
                # if target is between l and m, go left
                else: r = m - 1
            
            # m is in right sorted
            else:
                # if target is > r or < m, go left
                if target > nums[r] or target < nums[m]: r = m - 1
                # if target is between r and m, go right
                else: l = m + 1
            
        return -1