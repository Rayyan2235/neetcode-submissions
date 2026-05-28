class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        '''
        We are creating a minheap of size k therefore the kth value will be in the root
        heapify is a builtin func that sorts it such that the smallest value will be on the root node
        '''
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        while self.k < len(self.minheap):
            heapq.heappop(self.minheap)
                 

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0] # Will be 0 because thats where the root is. This is because,
        #We are creating a minheap of size k, so the smallest value will be the kth term, which will be the root

        
        

        
