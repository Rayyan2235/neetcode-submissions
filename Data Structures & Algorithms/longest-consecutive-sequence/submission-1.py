class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        newS = set(nums)
        longest = 0 # Counter

    # 'length' is the temporary counter for each iteration
        for n in newS:
            if n - 1 not in newS:
                # This n is a starting of a sequence number
                length = 1 # Sincei its the start of a sequence we init counter to 1

                while (n + length) in newS: # If there is a consecutive number after n
                    length += 1 # then increase counter. We keep comparing the same n with longest whioch keeps modifying based on the O(1) lookup if consec element in newS
                longest = max(length, longest)

        return longest
                




        