class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        
        longest = 0
        for x in nums:
            if x - 1 in st:
                continue
            
            length = 1
            while x + 1 in st:
                x = x + 1
                length += 1
            
            longest = max(longest, length)
        
        return longest