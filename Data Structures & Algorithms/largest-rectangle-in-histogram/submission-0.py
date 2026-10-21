class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []  # (start_index, height), heights increasing from bottom to top
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index  # current bar can extend back to where the popped bar started
            stack.append((start, h))

        # bars left in the stack extend all the way to the end
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area