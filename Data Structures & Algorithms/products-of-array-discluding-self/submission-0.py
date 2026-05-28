class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        n = len(nums)
        pre_mult = 1
        post_mult = 1
        
        prefix = [0] * n
        postfix = [0] * n

        for i in range(n):
            j = -i - 1 #This is to get the index of the opposite side of the number
            prefix[i] = pre_mult # We are going to update the pre_mult later on
            postfix[j] = post_mult

            # We are updating the prefix multiplier as we iterate from the left and then from the right using i and j
            pre_mult *=  nums[i]
            post_mult *= nums[j]

        return [l*r for l, r in zip(prefix, postfix)]

        