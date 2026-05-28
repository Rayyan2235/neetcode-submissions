class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
    BF SOLN:
    sort the arr i.e nums = [1,2,3,4,5]
    pop it k times i.e pop it k times
    return the kth pop
    i.e
        '''

        nums.sort()

        for i in range(k - 1):
            nums.pop()
        
        kth = nums.pop()
        return kth

        