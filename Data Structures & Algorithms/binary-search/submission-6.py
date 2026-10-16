class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # cond: <= target
        # TTTFFF last true
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mi = lo + (hi - lo + 1) // 2
            if nums[mi] <= target:
                lo = mi
            else:
                hi = mi - 1
        
        return lo if nums[lo] == target else -1