class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        
        longest = 0
        for x in nums:
            if x - 1 in st:
                continue
            
            end = x
            while end + 1 in st:
                end += 1
            
            longest = max(longest, end - x + 1)
        
        return longest