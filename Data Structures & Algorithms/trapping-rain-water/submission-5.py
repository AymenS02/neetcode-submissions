class Solution:
    def trap(self, height: List[int]) -> int:

        def scan(h):
            water = 0
            p1 = 0

            # Step 1: move p1 onto the first real block
            while p1 < len(h) and h[p1] == 0:
                p1 += 1

            p2 = p1 + 1
            negatives = 0

            while p2 < len(h):
                if h[p2] >= h[p1]:
                    # Step 5: found a wall as tall or taller, so close the pool
                    water += h[p1] * (p2 - p1 - 1) - negatives
                    p1 = p2
                    negatives = 0
                else:
                    # Steps 3 and 4: lower block (or empty), so store its height
                    negatives += h[p2]
                p2 += 1

            return water, p1

        # Left-to-right pass
        water, last = scan(height)

        # Right-to-left pass over whatever never got closed
        back, _ = scan(height[last:][::-1])

        return water + back





        # ai solution claude

        #         left, right = 0, len(height) - 1
        # left_max, right_max = height[left], height[right]
        # water = 0

        # while left < right:
        #     if left_max < right_max:
        #         left += 1
        #         left_max = max(left_max, height[left])
        #         water += left_max - height[left]
        #     else:
        #         right -= 1
        #         right_max = max(right_max, height[right])
        #         water += right_max - height[right]

        # return water