class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = defaultdict(int) # key: target - x, value: index

        for i, x in enumerate(nums):
            # check
            if x in hm:
                return [hm[x], i]
            
            # add
            hm[target - x] = i
        
        return -1