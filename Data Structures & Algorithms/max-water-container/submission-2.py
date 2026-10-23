class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights)-1

        area = 0

        while left < right:

            if min(heights[left], heights[right])*(right-left) > area:
                area = min(heights[left],heights[right])*(right-left)
                
                if heights[left] >= heights[right]:
                    right -= 1
                else:
                    left += 1
            
            elif heights[left] > heights[right]:

                right -= 1
            
            else:
                left += 1

        
        return area
            

            
