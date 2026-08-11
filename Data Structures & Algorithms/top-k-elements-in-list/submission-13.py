class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        K = 2 meaning the top 2 repeated items
        so if we heapify nums then remove such that there are k unique elements then 
        append it to new list

        '''

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # count => {1: 1, 2: 2, 3: 3} (unique number: freq)

        heap = []

        for i in count.keys(): # Iterate through the unique numbers to 
            heapq.heappush(heap, (count[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res