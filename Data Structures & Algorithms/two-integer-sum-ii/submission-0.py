class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        stack = []  # (value, index)

        for i, num in enumerate(numbers):
            while stack and stack[-1][0] + num > target:
                stack.pop()

            if stack and stack[-1][0] + num == target:
                return [stack[-1][1] + 1, i + 1]

            stack.append((num, i))