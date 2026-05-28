'''
Pattern: Most efficient is 2 pointers
Key Words: "1 Indexed" index starts from 1 rather than usual where it starts from 0
    "non-decreasing" means ascending, allows duplicates.

'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return[l + 1, r + 1]
           

    






        