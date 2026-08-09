class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # {1:1, 2:2, 3:3}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for i in count.keys(): # iterating through the unique numbers
            heapq.heappush(heap, (count[i], i)) # (frequency, value)
            if len(heap) > k: # want to restrict the heap size to k elements, this will remove the lowest count number.
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
