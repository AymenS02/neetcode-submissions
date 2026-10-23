class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            target = -nums[i]          # the pair must cancel out nums[i]
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]

                if total == target:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total > target:
                    right -= 1
                else:
                    left += 1

        return [list(t) for t in result]