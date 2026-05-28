class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0
        lmax, rmax = heights[l], heights[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, heights[l])
                res += lmax - heights[l]
            else:
                r-= 1
                rmax = max(rmax, heights[r])
                res += rmax -heights[r]
        return res
            
            
'''
            if heights[r - 1] < heights[r]:
                res += heights[r] - heights[r-1]
            else:
                r-=1
            
            if heights[l + 1] < heights[l]:
                res += heights[l] - heights[l + 1]
            else:
                l+= 1
        '''
'''if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1'''

            

        