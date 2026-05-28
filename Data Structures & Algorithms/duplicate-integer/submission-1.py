class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        real ={}

        for i in range(len(nums)):
            real[nums[i]] = 1 + real.get(nums[i], 0)

            for j in real.values():
                if j > 1:
                    return True
            

        return False







         