class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,1,1,2,2,3]

        # Created the dictionary [3: 1, 2: 2, 3: 1] (Key: cnt, Val: Actual number in nums)
        cnt = {}

        for num in nums:
            cnt[num] = 1 + cnt.get(num, 0)

        heap = []
        for num in cnt.keys():
            heapq.heappush(heap, (cnt[num], num )) # Heap = [cnt: Number]
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # Pop and append the Numebr to res (Not the count)

        return res


        