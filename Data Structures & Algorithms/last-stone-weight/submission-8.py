class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''-heapq.heapify(stones) - Thought this works but it doesnt because heapq return type is NONE therefore what we are doing instead is -NONE'''
        stones = [-s for s in stones]
        heapq.heapify(stones)
       

        while len(stones) > 1:
            fir = heapq.heappop(stones)
            sec = heapq.heappop(stones)

            if sec > fir:
                heapq.heappush(stones, fir-sec)
            
        stones.append(0)
        return abs(stones[0])
            

        