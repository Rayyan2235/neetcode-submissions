class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        '''Initialize the target k, the list of int nums
        we want to convert it into a heap'''
        heapq.heapify(self.minHeap)
        # we can initially have 0 
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    '''when we add a value, we want to insert it into the heap.
        We need to heappush it into the heap and that will sort it such that the smallest number will be on the top
        One way we can do is that we can have a minheap of size k
        This means that we pop out the largest number that is greater than k, because regardless of what number is added
        -that largest number will never be affected so we can just pop that out'''

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0] # we return the number on the top of the queue (the smallest number)

        '''when we add a value, we want to insert it into the heap.
        We need to heappush it into the heap and that will sort it such that the smallest number will be on the top
        One way we can do is that we can have a minheap of size k
        This means that we pop out the largest number that is greater than k, because regardless of what number is added
        -that largest number will never be affected so we can just pop that out'''

        
