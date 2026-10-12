class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        has = set()

        for e in nums:
            if e in has:
                return True

            has.add(e)
        
        return False