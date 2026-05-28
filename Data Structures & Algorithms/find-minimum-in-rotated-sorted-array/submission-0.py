class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        pattern : Modified Binary search. Because we are given a rotated array. We are asked to find the minimum num
        therefore thats the 'target' but we dont really know where the target is so we use the midpoint to compare with the boudnaries
        to figure out where in the array they are. We figure out which is sorted

        Mistakes:
         Thought we were looking for a specific target. But couldnt solve it that way 


        '''

        l = 0 
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break  # this is like an edge case, basically if alr sorted

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] > nums[r]: # [3,4,5,6,1,2]
                l = m + 1

            else:
                r = m - 1
        return res


            
        