class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        has = {}

        for e in nums:
            if e in has:
                return True

            has[e] = 1
        
        return False