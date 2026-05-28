class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Pattern: Modified Binary search. Must compare w the boundaries 

        what do I compare the mid value w? The boundaries?


        while l less than = r
        mid point index calc = m

        lets first treat edge case :
         if nums[m] == target:
        return m

        if nums[l] < nums[r]:
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r =m - 1
            else:
                return nums[m]

        if mid value > right most value: this means that the LHS is sorted and the RHS is not ex. [...,6,1,2]
        # Since we know its sorted on the left side then LHS < mid and if target lies between it ez

            if target is >= LHS AND Target < MID val: (Means the target is in the sorted (Ascending order) side)
                r = m -1
            else:
                l = m + 1
        else:
            if target <= RHS AND target > MID val:
                l = m + 1
            else:
                r = m - 1
    return -1

        '''

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            #Gonna treat the edge case, if array NOT rotated
            if nums[l] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m 

            if nums[m] > nums[r]: # This means that the LHS is sorted
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target<= nums[r] and target >nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

        