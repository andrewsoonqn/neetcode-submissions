class Solution:
    # l, r, mi
    # either l, mi
    # or mi, r
    # which is in the same segment will have l < mi - 1
    # or mi < r
    # find FIRST mi where [mi..r] is sorted but [l..mi] inclusive is not

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        first = -1

        while l <= r:
            mi = l + (r - l) // 2
            
            if nums[mi] < nums[-1]: # right segment is sorted
                first = mi
                r = mi - 1
            else: # left is sorted
                l = mi + 1
            

        return nums[first]