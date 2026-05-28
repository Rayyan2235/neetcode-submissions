class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            Need to return index of the sum of 2 numbers that add up to the target
            want to compare the pointers to sewe if they add up to the target
                if the sum is greater than target, we can move the right poitner and vice versa
                because this is a sorted array 

        '''
        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
