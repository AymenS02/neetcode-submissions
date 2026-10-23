class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1   # need a smaller sum
            else:
                left += 1    # need a bigger sum

        return []







        # stack solution if interested :)

        # stack = []  # (value, index)

        # for i, num in enumerate(numbers):
        #     while stack and stack[-1][0] + num > target:
        #         stack.pop()

        #     if stack and stack[-1][0] + num == target:
        #         return [stack[-1][1] + 1, i + 1]

        #     stack.append((num, i))