class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_lst = []

        for i in nums:
            if i in empty_lst:
                return True
            else:
                empty_lst.append(i)
            
        return False


         