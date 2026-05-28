class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        GOAL: Return max area ("Return the maximum amount of water a container can store.")
        Pattern: Brute force
        Logic: Iterated through all possible heights, we compared area formula for each 2 bars, and updated
            for every bigger area


        '''

        res = 0

        for i in range(len(heights)):

            for j in range(i + 1, len(heights)): # The formula below is the area
                res = max(res, min(heights[i], heights[j]) * (j - i)) # we are updating res everytime we get a bigger result

        return res

        

       