class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        MinH soln:
        1 soln: max heap
        pop it 
        '''

        nums = [-n for n in nums]
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)
            

        kth = heapq.heappop(nums)

        return -(kth)


  
        