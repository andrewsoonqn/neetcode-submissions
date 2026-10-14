class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        prev = 1
        res = [-1] * n
        res[n - 1] = prefix[n - 1]
        for i in range(n - 2, -1, -1):
            suffix = prev * nums[i + 1]
            res[i] = prefix[i] * suffix
            prev = suffix

        
        # print(f"{prefix=}")
        # print(f"{suffix=}")
        # print(f"{res=}")

        return res
