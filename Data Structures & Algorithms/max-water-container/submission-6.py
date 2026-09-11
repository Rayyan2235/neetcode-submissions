class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights) - 1
        max_A = 0

        while l < r:
            length = min(heights[l], heights[r]) # Minimum of the heights of the bars
            width =  r - l

            area = length * width
            max_A = max(max_A, area)

            if heights[l] > heights[r]: # We used an if statement because the output (r-=1) updates the length and wifth which is crucial so it must break out of it once the if condition is met once rather than using until we reach a condition (while)
                r -= 1
            else:
                l += 1
        return max_A


            

