class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        got to find 3 numbers that add up to 0     
        THIS IS BRUTE FORCE METHOD    
        '''
        res = set()
        nums.sort()
        
        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i] , nums[j] , nums[k]]
                        res.add(tuple(tmp))
        return list(res)

'''
✅ How Does nums.sort() Help?
By sorting the array before the loops, you ensure:

python
Copy
Edit
nums = [-4, -1, -1, 0, 1, 2]
Now:

When you pick i < j < k, you're always getting values in increasing value order

So [0, 1, -1] will never be generated — because -1 comes before 0 and 1 in the array

You’ll only get triplets like [-1, 0, 1], not [0, -1, 1] or [1, 0, -1]

This ensures the same numbers always appear in the same order, so the set doesn’t store permutations.'''

