class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 1 # since this is a possible starting number therefore starts w 1

                while (n + length) in numSet:
                    length += 1

                longest = max(length, longest)

        return longest




            
