class Solution:
    import math
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # left pass: res[i] = product of everything before i
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]

        # right pass: multiply in product of everything after i
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res