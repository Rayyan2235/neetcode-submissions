class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Max heap
        Pop k-1 elements 
        store the last pop which contains the kth element into a var
        return that var 

        '''

        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)

        result = -heapq.heappop(nums) # Convert all the negatives to positive and the positves to negatives due to max heap in first few lines

        return result
        