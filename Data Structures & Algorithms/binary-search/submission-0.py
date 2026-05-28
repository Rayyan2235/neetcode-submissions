class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        We need to find the midpoint
        if target greater than midpoint
        update  left pointer to m + 1'''

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2 # in java this would be an overload, watch the neetcode vid to udnerstand more 

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1




        
        
        