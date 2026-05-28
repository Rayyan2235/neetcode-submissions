class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        empty_dict = {}
        for i, j in enumerate(nums):
            difference = target - j

            if difference in empty_dict:
                return [empty_dict[difference], i]            
            
            empty_dict[j] = i

        