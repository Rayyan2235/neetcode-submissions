class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index,keys in enumerate(nums):
            difference = target - keys

            if difference in num_dict:
                return[num_dict[difference], index]
            
            num_dict[keys]=index
        