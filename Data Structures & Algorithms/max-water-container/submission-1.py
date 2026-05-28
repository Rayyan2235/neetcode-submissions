class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''
        GOAL: Return max area ("Return the maximum amount of water a container can store.")
        Pattern: 2 Pointers
        Logic: Kept one pointer in the start and in the end, whichever is the smaller heights
            has to move to the next or prior index. We compare and use res = max(res,) to
            keep updating the results
        Key Words: Max amount of water a container can store, this indiccates area



        '''
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area )
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
           
        return res


        

       