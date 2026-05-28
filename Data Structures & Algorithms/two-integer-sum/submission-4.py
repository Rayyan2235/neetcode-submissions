class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic ={}

        for i,j in enumerate(nums):
            difference = target - j

            if difference in dic:
                return[dic[difference], i]
            dic[j] = i